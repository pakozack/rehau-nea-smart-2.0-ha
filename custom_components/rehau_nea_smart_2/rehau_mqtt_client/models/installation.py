"""Type definitions for the installation data."""

from pydantic import BaseModel


class Cooling(BaseModel):
    """Type definition for cooling data."""

    normal: int
    reduced: int


class Heating(BaseModel):
    """Type definition for heating data."""

    normal: int
    reduced: int
    standby: int


class Setpoints(BaseModel):
    """Type definition for setpoints data."""

    cooling: Cooling
    heating: Heating
    min: int
    max: int


class Channel(BaseModel):
    """Type definition for channel data."""

    id: str
    target_temperature: int
    current_temperature: int
    energy_level: int
    operating_mode: int
    humidity: int
    demand: int
    setpoints: Setpoints


class Zone(BaseModel):
    """Type definition for zone data."""

    id: str
    name: str
    number: int
    channels: list[Channel]


class Group(BaseModel):
    """Type definition for group data."""

    id: str
    group_name: str
    zones: list[Zone]


class Installation(BaseModel):
    """Type definition for installation data."""

    id: str
    unique: str
    global_energy_level: int
    connected: bool
    operating_mode: int
    groups: list[Group]
    outside_temp: int
    outsideTempFiltered: int

class LiveEmu(BaseModel):
    unique: str
    pumpOn: bool
    mixed_circuit1_setpoint: int
    mixed_circuit1_supply: int
    mixed_circuit1_return: int
    mixed_circuit1_opening: int

class LiveDido(BaseModel):
    unique: str
    DI_1: bool
    DI_2: bool
    DI_3: bool
    DI_4: bool
    DI_5: bool
    DO_1: bool
    DO_2: bool
    DO_3: bool
    DO_4: bool
    DO_5: bool
