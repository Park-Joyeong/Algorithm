package datastructures.linkedlist;

import static com.google.common.truth.Truth.assertThat;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import org.junit.*;

public class DoublyLinkedListTest {
    private static final int LOOPS = 10000;
    private static final int TEST_SZ = 40;
    private static final int NUM_NULLS = TEST_SZ / 5;
    private static final int MAX_RAND_NUM = 250;

    DoublyLinkedList<Integer> list;

    @Before
    public void setup() {
        list = new DoublyLinkedList<>();
    }

    @Test
    public void testEmptyList() {
        assertThat(list.isEmpty()).isTrue();
        assertThat(list.size()).isEqualTo(0);
    }

}
