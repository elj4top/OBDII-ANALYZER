""" I don't have an ELM327 adapter or test vehicle yet, so obd_reader.py needs two modes:
 real connection, and a simulated one for development."""
import obd

class OBDReader:
    def __init__(self, simulate=False, port=None):
        self.simulate = simulate
        if not simulate:
            # port=None lets python-obd auto-detect the ELM327 adapter
            self.connection = obd.OBD(port)
        else:
            self.connection = None

    def get_live_data(self):
        if self.simulate:
            # fake but realistic values for test 
            # of the app before ever touching a real car
            return {
                "RPM": 850,
                "COOLANT_TEMP": 89,       # °C
                "SHORT_FUEL_TRIM_1": 2.3, # %
                "LONG_FUEL_TRIM_1": 8.6,  # % — trending positive, lean condition
                "THROTTLE_POS": 14.5,     # %
            }

        # Real mode: ask the adapter for each PID
        data = {}
        for cmd in [obd.commands.RPM, obd.commands.COOLANT_TEMP,
                    obd.commands.SHORT_FUEL_TRIM_1, obd.commands.LONG_FUEL_TRIM_1,
                    obd.commands.THROTTLE_POS]:
            response = self.connection.query(cmd)
            data[cmd.name] = response.value.magnitude if not response.is_null() else None
        return data

    def get_dtcs(self):
        if self.simulate:
            return ["P0171"]  # simulate a stored lean-condition code
        response = self.connection.query(obd.commands.GET_DTC)
        return [code for code, desc in response.value] if not response.is_null() else []