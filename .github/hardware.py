from enum import Enum


class FieldType(Enum):
    PIN = 0
    INT = 1
    BOOL = 2
    FLOAT = 3
    ARRAY = 4


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
    "ledidx_rgb_vtx": FieldType.ARRAY,
    "ledidx_rgb_boot": FieldType.ARRAY,
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
    "gsensor_stk8xxx": FieldType.BOOL,
    "thermal_lm75a": FieldType.BOOL,
    "pwm_outputs": FieldType.ARRAY,
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

field_groups = [
    # if one of the first group then all the first and second groups and
    # at-least one of the third group must also be defined
    [["serial_rx", "serial_tx"], [], []],
    [["radio_miso", "radio_mosi", "radio_sck", "radio_nss"], [], ["radio_rst", "pwm_outputs"]],
    [["radio_miso", "radio_mosi", "radio_sck", "radio_nss"], [], ["radio_dio0", "radio_dio1"]],
    [["radio_busy"], ["radio_miso", "radio_mosi", "radio_sck", "radio_nss", "radio_dio1"], []],
    [["radio_busy_2"], ["radio_miso", "radio_mosi", "radio_sck", "radio_nss_2", "radio_dio1_2"], []],
    [["radio_dio0"], ["radio_miso", "radio_mosi", "radio_sck", "radio_nss"], ["radio_rst", "pwm_outputs"]],
    [["radio_dio1"], ["radio_miso", "radio_mosi", "radio_sck", "radio_nss"], ["radio_rst", "pwm_outputs"]],
    [["radio_rst_2"], ["radio_miso", "radio_mosi", "radio_sck", "radio_nss", "radio_rst", "radio_nss_2"], []],
    [["radio_nss_2"], ["radio_miso", "radio_mosi", "radio_sck"], ["radio_dio0_2", "radio_dio1_2"]],
    [["power_min", "power_high", "power_max", "power_default", "power_control", "power_values"], [], []],
    [["debug_backpack_baud", "debug_backpack_rx", "debug_backpack_tx"], [], []],
    [["use_backpack"], ["debug_backpack_baud", "debug_backpack_rx", "debug_backpack_tx"], []],
    [["backpack_boot", "backpack_en"], ["use_backpack", "debug_backpack_baud", "debug_backpack_rx", "debug_backpack_tx"], []],
    [["i2c_scl", "i2c_sda"], [], []],
    [["joystick", "joystick_values"], [], []],
    [["five_way1", "five_way2", "five_way3"], [], []],
    [["misc_fan_pwm", "misc_fan_speeds"], [], []],
    [["vbat", "vbat_offset", "vbat_scale"], [], []],
    [["power_pdet", "power_pdet_intercept", "power_pdet_slope"], [], []],
    [["screen_sda"], ["screen_sck", "screen_type"], []],
    [["screen_mosi"], ["screen_cs", "screen_dc", "screen_rst", "screen_type", "screen_sck"], []],
    [["vtx_amp_pwm", "vtx_amp_vpd", "vtx_amp_vref", "vtx_nss", "vtx_miso", "vtx_mosi", "vtx_sck", "vtx_amp_vpd_25mW", "vtx_amp_vpd_100mW"], [], []]
]

mutually_exclusive_groups = [
    ["ant_ctrl", "ant_ctrl_compl"]
]

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
        had_error |= validate_grouping(target, layout, field)
    had_error |= validate_power_config(target, layout)
    had_error |= validate_backpack(target, layout)
    had_error |= validate_joystick(target, layout)
    return had_error


def validate_grouping(target, layout, field):
    had_error = False
    for group in field_groups:
        if field in group[0]:
            for must in group[0] + group[1]:
                if must not in layout:
                    print(f'device "{target}" because "{field}" is defined all other related fields must also be defined {must}')
                    print(f'\t{group[0] + group[1]}')
                    had_error = True
            found = True if group[2] == [] else False
            for one in group[2]:
                if one in layout:
                    found = True
            if not found:
                print(f'device "{target}" because "{field}" is defined at least one of the following fields must also be {group[2]}')
                had_error = True
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


def validate_backpack(target, layout):
    had_error = False
    if 'passthrough_baud' in layout:
        if layout['serial_rx'] == layout['serial_tx'] and layout['passthrough_baud'] != 230400:
            print(f'device "{target}" an external module with a backpack should set the baud rate to 230400')
            had_error = True
        if layout['serial_rx'] != layout['serial_tx'] and layout['passthrough_baud'] != 460800:
            print(f'device "{target}" an internal module with a backpack should set the baud rate to 460800')
            had_error = True
    return had_error


def validate_joystick(target, layout):
    had_error = False
    if 'joystick' in layout or 'joystick_values' in layout:
        if 'joystick' not in layout:
            print(f'device "{target}" joystick_values is defined so the joystick pin must also be defined')
            had_error = True
        elif 'joystick_values' not in layout:
            print(f'device "{target}" joystick is defined so the joystick_values must also be defined')
            had_error = True
        elif len(layout['joystick_values']) != 6:
            print(f'device "{target}" joystick_values must have 6 values defined')
            had_error = True
        else:
            for value in layout['joystick_values']:
                if value < 0 or value > 4095:
                    print(f'device "{target}" joystick_values must be between 0 and 4095 inclusive')
                    had_error = True
    return had_error
