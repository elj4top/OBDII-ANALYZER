import obd

class OBDReader:
    def __init__(self, simulate=False, port=None):
        self.simulate = simulate
        if not simulate:
            self.connection = obd.OBD(port)
        else:
            self.connection = None

    def get_live_data(self):
        if self.simulate:
            return {
                "RPM": 850,
                "COOLANT_TEMP": 89,
                "SHORT_FUEL_TRIM_1": 2.3,
                "LONG_FUEL_TRIM_1": 8.6,
                "THROTTLE_POS": 14.5,
            }

        data = {}
        for cmd in [obd.commands.RPM, obd.commands.COOLANT_TEMP,
                    obd.commands.SHORT_FUEL_TRIM_1, obd.commands.LONG_FUEL_TRIM_1,
                    obd.commands.THROTTLE_POS]:
            response = self.connection.query(cmd)
            data[cmd.name] = response.value.magnitude if not response.is_null() else None
        return data

    def get_dtcs(self):
        if self.simulate:
            return [("P0171", "System too Lean")]
        response = self.connection.query(obd.commands.GET_DTC)
        return response.value if not response.is_null() else []
