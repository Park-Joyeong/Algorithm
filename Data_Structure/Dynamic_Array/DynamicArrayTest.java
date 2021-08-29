package Data_Structure.Dynamic_Array;

import static com.google.common.truth.Truth.assertThat;

import org.junit.Test;

/**
 * DynamicArrayTest
 */
public class DynamicArrayTest {

  @Test
  public void testEmptyList() {
    DynamicArray<Integer> list = new DynamicArray<>();
    assertThat(list.isEmpty()).isTrue();
  }

  @Test(expected = Exception.class)
  public void testRemovingEmpty() {
    DynamicArray<Integer> list = new DynamicArray<>();
    list.removeAt(0);
  }

}