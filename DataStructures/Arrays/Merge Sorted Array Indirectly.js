// A bit different from the Python version.
// This problem creates a new array


function mergeSortedArrays(array1, array2) {   
  // the first three-if cases are if any array or both are empty
  if (!array1.length && !array2.length) {
      return [];
  }
  else if (!array1.length && array2.length !== 0) {
      return array2;
  } 
  else if (!array2.length && array1.length !== 0) {
      return array1;
  } 
  else {
      const mergedArray = [];
      let array1Item = array1[0];
      let array2Item = array2[0];
      let i = 1;
      let j = 1;

      while (array1Item || array2Item){
          if(array2Item === undefined || array1Item < array2Item){
            mergedArray.push(array1Item);
            array1Item = array1[i];
            i++;
          }   
          else {
            mergedArray.push(array2Item);
            array2Item = array2[j];
            j++;
          }
         }
         console.log(mergedArray);
         return mergedArray;
  }
}


mergeSortedArrays([1, 8, 10, 38], [2, 9, 31]);


  
