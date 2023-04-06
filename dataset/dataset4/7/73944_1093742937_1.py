@format_to_string    
@mappedclass(clipper_core.Cell_descr)
class Cell_descr(clipper_core.Cell_descr):
    def __init__(self, abc, angles):
        '''
        __init__(self, abc, angles) -> Cell_descr
        
        Args:
            abc ([float*3]): cell dimensions in Angstroms
            angles ([float*3]): alpha, beta and gamma angles in degrees
        '''
        clipper_core.Cell_descr.__init__(self, *abc, *angles)
    
@format_to_string
@getters_to_properties('cell_descr', 'matrix_frac', 'matrix_orth', 
                       'metric_real', 'metric_reci', 'volume')
@mappedclass(clipper_core.Cell)
class Cell(clipper_core.Cell):
    '''
    Define a crystallographic unit cell using the lengths of the three
    sides a, b, c (in Angstroms) and the three angles alpha, beta, gamma
    (in degrees). 
    '''
    def __init__(self, abc, angles):
        '''
        __init__(self, abc, angles) -> Cell
        
        Args:
            abc ([float*3]): cell dimensions in Angstroms
            angles ([float*3]): alpha, beta and gamma angles in degrees
        '''
        cell_descr = Cell_descr(abc, angles)
        #cell_descr = clipper_core.Cell_descr(*abc, *angles)
        clipper_core.Cell.__init__(self, cell_descr)
    
    def __eq__(self, other):
        return self.equals(other)