from math import sqrt
import json

class AudioInfo: pass

class BatteryInfo: pass

class CameraInfo: pass

class Contact:
    def __init__(self, info):
        self._raw = info

    def __repr__(self):
        redacted_name = self.name[0] + "*****" if self.name else "Unknown"
        redacted_number = f"{self.number[:3]}*****{self.number[-2:]}" if self.number else "No Number"
        return f"<Contact name='{redacted_name}' number='{redacted_number}'>"

    def __eq__(self, other):
        if isinstance(other, Contact):
            return (self.name, self.number) == (other.name, other.number)
        return NotImplemented

    @property
    def name(self) -> str:
        """Name of a contact"""
        return self._raw["name"]

    @property
    def number(self) -> str:
        """Number of a contact"""
        return self._raw["number"]

class Job: pass

class LocationInfo:
    def __init__(self, raw):
        self._raw = json.loads(raw)

    def __repr__(self):
        return f"<Location object at {hex(id(self))}>"

    def __eq__(self, other):
        if isinstance(other, LocationInfo):
            return (
                abs(self.lat - other.lat) < 1e-9 and
                abs(self.long - other.long) < 1e-9 and
                abs(self.alt - other.alt) < 1e-3
            )
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, LocationInfo):
            dlat = self.lat - other.lat
            dlong = self.long - other.long
            dalt = self.alt - other.alt
            return (dlat, dlong, dalt)
        return NotImplemented

    def distance_to(self, other):
        if isinstance(other, LocationInfo):
            return sqrt(
                (self.lat - other.lat) ** 2 +
                (self.long - other.long) ** 2 +
                (self.alt - other.alt) ** 2
            )
        raise TypeError("distance_to expects another LocationInfo object")

    @property
    def long(self) -> float:
        """Longitude"""
        return self._raw["longitude"]

    @property
    def longitude(self) -> float:
        """Longitude"""
        return self.long

    @property
    def lat(self) -> float:
        """Latitude"""
        return self._raw["latitude"]

    @property
    def latitude(self) -> float:
        """Latitude"""
        return self.lat

    @property
    def alt(self) -> float:
        """Altitude"""
        return self._raw["altitude"]

    @property
    def altitude(self) -> float:
        """Altitude"""
        return self.alt

    @property
    def vertical_accuracy(self) -> float:
        """Vertical accuracy"""
        return self._raw["vertical_accuracy"]

    @property
    def bearing(self) -> float:
        """Bearing in degress"""
        return self._raw["bearing"]

    @property
    def speed(self) -> float:
        """Speed in m/s"""
        return self._raw["speed"]

    @property
    def elapsed(self) -> int:
        """How long it takes to get the location, in miliseconds"""
        return self._raw["elapsedMs"]

    @property
    def provider(self) -> str:
        """Provider of location, either of gps or network"""
        return self._raw["provider"]

    @property
    def is_gps(self) -> bool:
        """True if provider is GPS"""
        return self._raw["provider"].lower() == "gps"

    @property
    def is_network(self) -> bool:
        """True if provider is from network"""
        return self._raw["provider"].lower() == "network"

class KeystoreInfo: pass

class MediaPlayerInfo: pass

class NfcInfo: pass

class SensorInfo: pass
