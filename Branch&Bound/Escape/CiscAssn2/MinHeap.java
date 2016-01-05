package CiscAssn2;
//Hassan Haq
//10061306
//12huh
//The min heap class implemented to make a...well min heap
public class MinHeap

{
  public partialSolution[] Heap;
  private int size;
  private static final int FRONT = 1;
  public MinHeap()
  {
      this.size = 0;
      Heap = new partialSolution[100000000];
      Heap[0] = new partialSolution("0",Integer.MIN_VALUE,0);
  }

  private int parent(int pos)
  {
      return pos / 2;
  }

  private int leftChild(int pos)
  {
      return (2 * pos);
  }

  private int rightChild(int pos)

  {
      return (2 * pos) + 1;
  }

  private boolean isLeaf(int pos)
  {
      if (pos >=  (size / 2)  &&  pos <= size)
      { 
          return true;
      }
      return false;
  }

  private void swap(int fpos, int spos)
  {
      partialSolution tmp;
      tmp = Heap[fpos];
      Heap[fpos] = Heap[spos];
      Heap[spos] = tmp;
  }

  private void minHeapify(int pos)
  {
      if (!isLeaf(pos))
      { 
          if ( Heap[pos].lB > Heap[leftChild(pos)].lB  || Heap[pos].lB > Heap[rightChild(pos)].lB)
          {
              if (Heap[leftChild(pos)].lB < Heap[rightChild(pos)].lB)
              {
                  swap(pos, leftChild(pos));
                  minHeapify(leftChild(pos));
              }
              else
              {
                  swap(pos, rightChild(pos));
                  minHeapify(rightChild(pos));
              }
          }
      }
  }

  public void insert(partialSolution ele)
  {
      Heap[++size] = ele;
      int current = size;
      while (Heap[current].lB < Heap[parent(current)].lB)
      {
          swap(current,parent(current));
          current = parent(current);
      }	
  }

  public void print()
  {
      for (int i = 1; i <= size / 2; i++ )
      {
          System.out.print(" PARENT : " + Heap[i].lB + " LEFT CHILD : " + Heap[2*i].lB 
              + " RIGHT CHILD :" + Heap[2 * i  + 1].lB);
          System.out.println();
      } 
  }

  public void minHeap()
  {
      for (int pos = (size / 2); pos >= 1 ; pos--)
      {
          minHeapify(pos);
      }
  }

  public partialSolution remove()
  {
      partialSolution popped = Heap[FRONT];
      Heap[FRONT] = Heap[size--]; 
      minHeapify(FRONT);
      return popped;
  }

  public static void main(String arg[])
  {
  }

}
