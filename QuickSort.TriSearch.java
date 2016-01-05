
import java.util.Random;


public class tst {
//class var.
//the size of the random integer array and the testing array can be changed for each run,
public static int n = 7000;
public static int k = n/10;
//generating random array
	public static int [] randArray(){
		int[] Arr = new int[n];	
		int randNum;
		Random rand = new Random();
		for(int i = 0; i < n; i++){
			//generates a random number between 0 and n and puts it into the array
			//this is also a precursor for how I generate numbers that are not in the array
			randNum = rand.nextInt(n);
			Arr[i] = randNum;
		}
		return Arr;
	}
//Method to do the Quick Sort
	public static void quickSort(int[] arr, int low, int high){
		if ( arr == null || arr.length == 0){
			return;
		}
		if (low >= high){
			return;
		}
		int middle = low +(high - low)/2;
		int pivot = arr[middle];
		
		int i = low, j = high;
		while ( i <= j){
			while ( arr [i] < pivot){
				i++;
			}
			
			while ( arr[j] > pivot){
				j --;
			}
			if ( i <= j) {
				int temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
				i++;
				j--;
			}
		}
		if (low<j){
			quickSort(arr, low, j);
		}
		if (high > i){
			quickSort(arr, i, high);
		}
	}
	//Method for the Binary Search
	public static boolean binarySearch(int[] arr, int key, int low, int high){

		while (high >= low){
			int middle = (low + high) /2;
			if(arr[middle] == key) {
				return true;
			}
			if (arr[middle]< key){
				low = middle + 1;
			}
			if (arr[middle] > key){
				high = middle - 1;
			}
		}
		return false;
	}
	//Method for Trinary Search
	public static boolean trinarySearch (int [] arr, int key, int low, int high){
		if (low > high)
			return false;
		int mid1 = low + (high - low)/3;
		int mid2 = low + 2*(high - low) / 3;
		if (arr[mid1] == key)
			return true;
		else if (arr[mid2] == key)
			return true;
		else if (key < arr[mid1])
			return trinarySearch (arr,key, low, mid1-1);
		else if (key > arr[mid2])
			return trinarySearch(arr,key, mid2+1, high);
		else 
			return trinarySearch (arr,key, mid1, mid2);

	}
	//finding the time it takes to run a binary search on an array (arr) of size n 
	//finding values in/not in the array(srch) or size k
	public static long binTime(int [] arr, int []srch){

		long endTime;
		long startTime = System.nanoTime();
		int low = 0;
		int high = arr.length - 1;
		for (int j = 0; j < k; j++){
			binarySearch(arr, srch[j], low, high);
		}
		endTime = System.nanoTime();
		long biTime = endTime - startTime;
		
		return biTime;

	//finding the time it takes to run a trinary search on an array (arr) of size n 
	//finding values in/not in the array(srch) or size k
	}
	public static long triTime(int [] arr, int []srch){

		long endTime;
		long startTime = System.nanoTime();
		int low = 0;
		int high = arr.length - 1;
		for (int j = 0; j < k; j++){
			trinarySearch(arr, srch[j], low, high);
		}
		endTime = System.nanoTime();
		long biTime = endTime - startTime;
		
		return biTime;
		
	}

	//Main Method
	public static void main (String [] args){
		//initializing the array of random integers, the array has values between 0 and n
		int[] arr = randArray();
		int low = 0;
		int high = arr.length - 1;
		//Sorting the random array
		quickSort(arr, low, high);
		//experiment1
		//Finding random values with in the array 
		Random in = new Random();
		int[] srchVal = new int[k];
		//filling the array with k values, we generate a random number between 0 -> n (size of our random integers array)
		//we then use that number as the index to give a random value from the list to our array of k values
		for (int i = 0; i < k; i ++){
			int randVal = in.nextInt(n);
			srchVal[i] = arr[randVal];
		}
		//calling binary and trinary search with our random array and the array of k values from the random array
		long biTime = binTime(arr, srchVal);
		long triTime = triTime (arr, srchVal);
		
		
		//experiment 2: searching for values not in the array
		int[] arr2 = randArray();
		//creating a second array of random integers and changing all odd numbers to even numbers
		for (int a = 0; a < n; a++){
			if (arr2[a]%2 != 0){
				arr2[a] = arr2[a]+1;
			}
		}
		//generating an array of k values that are all odd numbers and could not exist in arr[2]
		int [] greatVal = new int [k];
		Random odd = new Random();
		for (int b = 0; b < k; b++){
			int randNum = odd.nextInt(n);
			if (randNum%2 != 0){
				greatVal[b] = randNum;
			}
			else {
				greatVal[b] = randNum+1;
			}
		}
		//calling binary and trinary search with our array of even integes and the corresponding array of odd integers
		long biTimeEx2 = binTime (arr2, greatVal);
		long triTimeEx2 = triTime (arr2, greatVal );
		
		
		System.out.println("Time for values in the array:");
		System.out.println ("The time for the binary search was: " + biTime);
		System.out.println ("The time for the trinary search was: " + triTime);
		System.out.println("Time for values not in the array:");
		System.out.println ("The time for the binary search was: " + biTimeEx2);
		System.out.println ("The time for the trinary search was: " + triTimeEx2);
		
		
	}
}
