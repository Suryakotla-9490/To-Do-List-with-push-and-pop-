import numpy as np
import array
class array1(array.array):
     arraynumber1=np.array(((2,3,4),(5,6,7),(4,6,8)))
     arraynumber2 = np.array([[3,2,5],[9,7,8],[5,9,6]])
     def array_addtion(self):
         resultarray = self.arraynumber1+self.arraynumber2
         print("the array_addition function retunse the retun array")
         return resultarray



arrayobj = array1("u")
#arrayobj.arraynumber1 =np.array([[1,2,3],[5,5,6]])
#arrayobj.arraynumber2 = np.array([[7,8,9],[1,5,8]])
resultarray = arrayobj.array_addtion()
print("array after addition:\n",r`esultarray) 