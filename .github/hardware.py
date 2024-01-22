from enum import Enum


class FieldType(Enum):
    PIN = 0
    INT = 1
    BOOL = 2
    FLOAT = 3
    ARRAY = 4
    COUNT = 5


hardware_fields = {
    "serial_rx": FieldType.PIN,
    "serial_tx": FieldType.PIN,
    "radio_busy": FieldType.PIN,
    "radio_busy_2": FieldType.PIN,
    "radio_dio0": FieldType.PIN,
    "radio_dio0_2": FieldType.PIN,
    "radio_dio1": FieldType.PIN,
    "radio_dio1_2": FieldType.PIN,
    "radio_dio2": FieldType.PIN,
    "radio_miso": FieldType.PIN,
    "radio_mosi": FieldType.PIN,
    "radio_nss": FieldType.PIN,
    "radio_nss_2": FieldType.PIN,
    "radio_rst": FieldType.PIN,
    "radio_rst_2": FieldType.PIN,
    "radio_sck": FieldType.PIN,
    "radio_dcdc": FieldType.BOOL,
    "radio_rfo_hf": FieldType.BOOL,
    "ant_ctrl": FieldType.PIN,
    "ant_ctrl_compl": FieldType.PIN,
    "power_enable": FieldType.PIN,
    "power_apc1": FieldType.PIN,
    "power_apc2": FieldType.PIN,
    "power_rxen": FieldType.PIN,
    "power_txen": FieldType.PIN,
    "power_rxen_2": FieldType.PIN,
    "power_txen_2": FieldType.PIN,
    "power_lna_gain": FieldType.INT,
    "power_min": FieldType.INT,
    "power_high": FieldType.INT,
    "power_max": FieldType.INT,
    "power_default": FieldType.INT,
    "power_pdet": FieldType.PIN,
    "power_pdet_intercept": FieldType.FLOAT,
    "power_pdet_slope": FieldType.FLOAT,
    "power_control": FieldType.INT,
    "power_values": FieldType.ARRAY,
    "power_values2": FieldType.ARRAY,
    "power_values_dual": FieldType.ARRAY,
    "joystick": FieldType.PIN,
    "joystick_values": FieldType.ARRAY,
    "five_way1": FieldType.PIN,
    "five_way2": FieldType.PIN,
    "five_way3": FieldType.PIN,
    "button": FieldType.PIN,
    "button_led_index": FieldType.INT,
    "button2": FieldType.PIN,
    "button2_led_index": FieldType.INT,
    "led": FieldType.PIN,
    "led_blue": FieldType.PIN,
    "led_blue_invert": FieldType.BOOL,
    "led_green": FieldType.PIN,
    "led_green_invert": FieldType.BOOL,
    "led_green_red": FieldType.PIN,
    "led_red": FieldType.PIN,
    "led_red_invert": FieldType.BOOL,
    "led_red_green": FieldType.PIN,
    "led_rgb": FieldType.PIN,
    "led_rgb_isgrb": FieldType.BOOL,
    "ledidx_rgb_status": FieldType.ARRAY,
    "ledidx_rgb_status_count": FieldType.COUNT,
    "ledidx_rgb_vtx": FieldType.ARRAY,
    "ledidx_rgb_vtx_count": FieldType.COUNT,
    "ledidx_rgb_boot": FieldType.ARRAY,
    "ledidx_rgb_boot_count": FieldType.COUNT,
    "screen_cs": FieldType.PIN,
    "screen_dc": FieldType.PIN,
    "screen_mosi": FieldType.PIN,
    "screen_rst": FieldType.PIN,
    "screen_sck": FieldType.PIN,
    "screen_sda": FieldType.PIN,
    "screen_type": FieldType.INT,
    "screen_reversed": FieldType.BOOL,
    "screen_bl": FieldType.PIN,
    "use_backpack": FieldType.BOOL,
    "debug_backpack_baud": FieldType.INT,
    "debug_backpack_rx": FieldType.PIN,
    "debug_backpack_tx": FieldType.PIN,
    "backpack_boot": FieldType.PIN,
    "backpack_en": FieldType.PIN,
    "passthrough_baud": FieldType.INT,
    "i2c_scl": FieldType.PIN,
    "i2c_sda": FieldType.PIN,
    "misc_gsensor_int": FieldType.PIN,
    "misc_buzzer": FieldType.PIN,
    "misc_fan_en": FieldType.PIN,
    "misc_fan_pwm": FieldType.PIN,
    "misc_fan_tacho": FieldType.PIN,
    "misc_fan_speeds": FieldType.ARRAY,
    "misc_fan_speeds_count": FieldType.COUNT,
    "gsensor_stk8xxx": FieldType.BOOL,
    "thermal_lm75a": FieldType.BOOL,
    "pwm_outputs": FieldType.ARRAY,
    "pwm_outputs_count": FieldType.COUNT,
    "vbat": FieldType.PIN,
    "vbat_offset": FieldType.INT,
    "vbat_scale": FieldType.INT,
    "vbat_atten": FieldType.INT,
    "vtx_amp_pwm": FieldType.PIN,
    "vtx_amp_vpd": FieldType.PIN,
    "vtx_amp_vref": FieldType.PIN,
    "vtx_nss": FieldType.PIN,
    "vtx_miso": FieldType.PIN,
    "vtx_mosi": FieldType.PIN,
    "vtx_sck": FieldType.PIN,
    "vtx_amp_vpd_25mW": FieldType.ARRAY,
    "vtx_amp_vpd_100mW": FieldType.ARRAY
}


allowable_duplicates = [
    ['serial_rx', 'serial_tx'],
    ['screen_sck', 'i2c_scl'],
    ['screen_sda', 'screen_mosi', 'i2c_sda']
]


used_pins = {}


def validate(target, layout):
    global used_pins
    had_error = False
    used_pins = {}
    for field in layout:
        # Ensure that the layout field is a valid field from the hardware list
        if field not in hardware_fields.keys():
            print(f'device "{target}" has an unknown field name {field}')
            had_error = True
        else:
            had_error |= validate_pin_uniqueness(target, layout, field)
    had_error |= validate_power_config(target, layout)
    return had_error


def validate_pin_uniqueness(target, layout, field):
    had_error = False
    if hardware_fields[field] == FieldType.PIN:
        pin = layout[field]
        if pin in used_pins.keys():
            allowed = False
            for duplicate in allowable_duplicates:
                if field in duplicate and used_pins[pin] in duplicate:
                    allowed = True
            if not allowed:
                print(f'device "{target}" PIN {pin} "{field}" is already assigned to "{used_pins[pin]}"')
                had_error = True
        else:
            used_pins[pin] = field
    return had_error


def validate_power_config(target, layout):
    had_error = False
    if 'power_values' in layout:
        power_values = layout['power_values']
        power_max = layout['power_max']
        power_min = layout['power_min']
        power_default = layout['power_default']
        power_high = layout['power_high']
        if power_min > power_max:
            print(f'device "{target}" power_min must be less than or equal to power_max')
            had_error = True
        if power_default < power_min or power_default > power_max:
            print(f'device "{target}" power_default must lie between power_min and power_max')
            had_error = True
        if power_high < power_min or power_high > power_max:
            print(f'device "{target}" power_high must lie between power_min and power_max')
            had_error = True
        if power_max-power_min+1 != len(power_values):
            print(f'device "{target}" power_values must have the correct number of entries to match all values from power_min to power_max')
            had_error = power_max-power_min+1 > len(power_values)
        if layout['power_control'] == 3 and 'power_apc2' not in layout:
            print(f'device "{target}" defines power_control as DACWRITE and power_apc2 is undefined')
            had_error = True
        if 'power_values2' in layout:
            if len(layout['power_values2']) != len(power_values):
                print(f'device "{target}" power_values2 must have the same number of entries as power_values')
                had_error = True
            if layout['power_control'] != 3:
                print(f'device "{target}" power_values2 is defined so power_control must be set to 3 (DACWRITE)')
                had_error = True
            if 'power_apc2' not in layout:
                print(f'device "{target}" power_values2 is defined so the power_apc2 pin must also be defined')
                had_error = True
    return had_error
