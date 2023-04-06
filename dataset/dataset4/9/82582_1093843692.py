
@dataclasses.dataclass
class SpectralData:
    """Class to hold data and metadata from a fiber spectrograph."""
    wavelength: astropy.units.Quantity
    """The wavelength array produced by the instrument."""
    spectrum: np.ndarray
    """The flux array in instrumental units."""
    duration: float
    """The duration of the exposure in seconds."""
