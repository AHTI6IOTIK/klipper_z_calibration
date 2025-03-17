import stepper
from mcu import MCU_endstop

class KobraProbe:
    def __init__(self, config):
        self.config = config
        self.printer = config.printer
        self.stepper = None

        conf_pin = config.get('pin')

        ppins = config.printer.lookup_object('pins')
        self.endstop_pin = ppins.setup_pin('endstop', conf_pin)

        mcu = config.printer.lookup_object('mcu')
        pin_params = ppins.parse_pin(conf_pin)
        self.mcu_endstop = MCU_endstop(mcu, pin_params)
        self.printer.register_event_handler("homing:home_rails_end", self.handle_home_rails_end)

    def handle_home_rails_end(self, homing_state, rails):
        for rail in rails:
            stepper = rail.get_steppers()[0]
            if stepper.is_active_axis('z'):
                self.mcu_endstop.add_stepper(stepper)
                return

    def get_mcu_endstop(self):
        return self.mcu_endstop

def load_config(config):
    return KobraProbe(config)
