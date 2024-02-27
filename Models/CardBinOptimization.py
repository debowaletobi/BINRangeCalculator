from Models.Exceptions import IncorrectBinDataType,LowerBoundGreaterThanUpperBoundError,PanLengthError
#import Models

class OptimizeBinRanging():
    
    def __init__(self, bin_lower_bound, bin_upper_bound, pan_length=16):
        self._bin_lower_bound = OptimizeBinRanging.check_bin_data_type(bin_lower_bound,'Bin lower bound must be an integer')                                                                 
        self._bin_upper_bound = OptimizeBinRanging.check_bin_data_type(bin_upper_bound,'Bin upper bound must be an integer')
        OptimizeBinRanging.validate_lower_upper_bound_combination(bin_lower_bound, bin_upper_bound)
        self._pan_length = OptimizeBinRanging.check_pan_length(pan_length)
        self._core_bin = OptimizeBinRanging.get_core_bin(self._bin_lower_bound, self._bin_upper_bound)
        self._pan_length = pan_length 
        
                                                                        
    @staticmethod    
    def check_bin_data_type(_bin, error_message):
        if not isinstance(_bin, int):
            raise IncorrectBinDataType(error_message)
        return _bin
      
    
    @staticmethod
    def validate_lower_upper_bound_combination(lower_bound, upper_bound):
        error_message = "Ensure the bin lower bound value is less than the upper bound value"                                                     
        if lower_bound>upper_bound:
            raise LowerBoundGreaterThanUpperBoundError(error_message)
          
        
    @staticmethod
    def get_core_bin(bin_lower_bound, bin_upper_bound):
        bin_lower_bound = str(bin_lower_bound)
        bin_upper_bound = str(bin_upper_bound)
        _core_bin = ''
        i =0
        while i<len(bin_lower_bound):
            if bin_lower_bound[i]==bin_upper_bound[i]:
                _core_bin += bin_lower_bound[i]
                i+=1
            else:
                break
        return _core_bin
    
    
    @property
    def core_bin(self):
        return self._core_bin
    
    
    @property
    def core_bin_length(self):
        return len(str(self._core_bin))
    
    
    @staticmethod
    def check_pan_length(pan_length):
        if pan_length==16 or pan_length ==19:
            return pan_length
        raise PanLengthError("Invalid PAN length passed. Ensure PAN length is equal to 16 or 19")
     
    
    @property
    def pan_length(self):
        return self._pan_length
    
    
    @pan_length.setter
    def pan_length(self, new_pan_length):
        OptimizeBinRanging.check_pan_length(new_pan_length) 
        self._pan_length = new_pan_length
     

    def get_flexible_part_combinations(self):
        flexible_part = self.pan_length - len(str(self._bin_upper_bound))
        combinations = 10**(flexible_part-1)
        return int(combinations)
     
        
    @staticmethod    
    def get_digit_without_leading_zero(digit):
        digit = str(digit)
        if len((digit))==1 or digit[0]!='0':
                return int(digit)
        return OptimizeBinRanging.get_digit_without_leading_zero(digit[1:])
     
       
    def get_fixed_flexible_part(self):
        i = self.core_bin_length
        try:
            lower = OptimizeBinRanging.get_digit_without_leading_zero(str(self._bin_lower_bound)[i:])
        except IndexError:
            lower=0
        try:
            upper = int(str(self._bin_upper_bound)[i:])
        except ValueError:
            upper=0
        return upper-lower+1
    
    @property
    def no_cards_possible(self):
        print('no_of_cards_possible called')
        return int(self.get_fixed_flexible_part()*self.get_flexible_part_combinations())
