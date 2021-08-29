package Data_Structure.Dynamic_Array;

import java.util.Iterator;

/**
 * DynamicArray
 */
@SuppressWarnings("unchecked")
public class DynamicArray<T> implements Iterable<T> {

  private T[] arr;
  private int len = 0; // length user thinks array is
  private int capacity = 0; // Actual array size

  public DynamicArray() {
    this(16);
  }

  public DynamicArray(int capacity) {
    if (capacity < 0)
      throw new IllegalArgumentException("Illegal Capacity: " + capacity);
    this.capacity = capacity;
    arr = (T[]) new Object[capacity];
  }

  public int size() {
    return len;
  }

  public boolean isEmpty() {
    return size() == 0;
  }

  public T get(int index) {
    if (index >= len || index < 0)
      throw new IndexOutOfBoundsException();
    return arr[index];
  }

  public void set(int index, T elem) {
    if (index >= len || index < 0)
      throw new IndexOutOfBoundsException();
    arr[index] = elem;
  }

  public void clear() {
    for (int i = 0; i < len; i++)
      arr[i] = null;
    len = 0;
  }

  public void add(T elem) {

    // Time to resize
    if (len + 1 >= capacity) {
      if (capacity == 0)
        capacity = 1;
      else
        capacity *= 2; // double the size
      T[] new_arr = (T[]) new Object[capacity];
      for (int i = 0; i < len; i++)
        new_arr[i] = arr[i];
      arr = new_arr;
    }

    arr[len++] = elem;
  }

  // Removes an element at the specified index in this array.
  public T removeAt(int rm_index) {
    // TODO
    // if (rm_index == 0)
    //   throw new IndexOutOfBoundsException();
    return null;
  }

  @Override
  public Iterator<T> iterator() {
    // TODO Auto-generated method stub
    return null;
  }
}