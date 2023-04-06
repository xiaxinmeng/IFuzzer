import random                                                         
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor    
from time import sleep    
                        
def worker():           
    with ProcessPoolExecutor() as pool:      
        r = list(pool.map(sleep, [0.01] * 8))       
                                                    
                                                   
if __name__ == '__main__':                         
    pool = ThreadPoolExecutor()     
                                   
    i = 0                          
    while True:                    
        if random.random() < 0.9:                    
            pool.submit(sleep, 0.001)      
        else:                             
            r = pool.submit(worker)         
            r = r.result()                
        i += 1                           
        print('alive', i)