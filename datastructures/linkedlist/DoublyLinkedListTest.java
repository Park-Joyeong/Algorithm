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

    @Test(expected = Exception.class)
    public void testRemoveFirstOfEmpty() {
        list.removeFirst();
    }

    @Test(expected = Exception.class)
    public void testRemoveLastOfEmpty() {
        list.removeLast();
    }

    @Test(expected = Exception.class)
    public void testPeekFirstOfEmpty() {
        list.peekFirst();
    }

    @Test(expected = Exception.class)
    public void testPeekLastOfEmpty() {
        list.peekLast();
    }

    @Test
    public void testAddFirst() {
        list.addFirst(3);
        assertThat(list.size()).isEqualTo(1);
        list.addFirst(5);
        assertThat(list.size()).isEqualTo(2);
    }

    @Test
    public void testAddLast() {
        list.addLast(3);
        assertThat(list.size()).isEqualTo(1);
        list.addLast(5);
        assertThat(list.size()).isEqualTo(2);
    }

    @Test
    public void testAddAt() throws Exception {
        list.addAt(0, 1);
        assertThat(list.size()).isEqualTo(1);
        list.addAt(1, 2);
        assertThat(list.size()).isEqualTo(2);
        list.addAt(1, 3);
        assertThat(list.size()).isEqualTo(3);
        list.addAt(2, 4);
        assertThat(list.size()).isEqualTo(4);
        list.addAt(1, 8);
        assertThat(list.size()).isEqualTo(5);
    }

    @Test
    public void testRemoveFirst() {
        list.addFirst(3);
        assertThat(list.removeFirst()).isEqualTo(3);
        assertThat(list.isEmpty()).isTrue();
    }

    @Test
    public void testRemoveLast() {
        list.addLast(4);
        assertThat(list.removeLast()).isEqualTo(4);
        assertThat(list.isEmpty()).isTrue();
    }

    @Test
    public void testPeekFirst() {
        list.addFirst(4);
        assertThat(list.peekFirst()).isEqualTo(4);
        assertThat(list.size()).isEqualTo(1);
    }

    @Test
    public void testPeekLast() {
        list.addLast(4);
        assertThat(list.peekLast()).isEqualTo(4);
        assertThat(list.size()).isEqualTo(1);
    }

    @Test
    public void testPeeking() {
        // 5
        list.addFirst(5);
        assertThat(list.peekFirst()).isEqualTo(5);
        assertThat(list.peekLast()).isEqualTo(5);

        // 6 - 5
        list.addFirst(6);
        assertThat(list.peekFirst()).isEqualTo(6);
        assertThat(list.peekLast()).isEqualTo(5);

        // 7 - 6 - 5
        list.addFirst(7);
        assertThat(list.peekFirst()).isEqualTo(7);
        assertThat(list.peekLast()).isEqualTo(5);

        // 7 - 6 - 5 - 8
        list.addLast(8);
        assertThat(list.peekFirst()).isEqualTo(7);
        assertThat(list.peekLast()).isEqualTo(8);

        // 7 - 6 - 5
        list.removeLast();
        assertThat(list.peekFirst()).isEqualTo(7);
        assertThat(list.peekLast()).isEqualTo(5);

        // 7 - 6
        list.removeLast();
        assertThat(list.peekFirst()).isEqualTo(7);
        assertThat(list.peekLast()).isEqualTo(6);

        // 6
        list.removeFirst();
        assertThat(list.peekFirst()).isEqualTo(6);
        assertThat(list.peekLast()).isEqualTo(6);
    }

    @Test
    public void testRemoving() {
        DoublyLinkedList<String> strs = new DoublyLinkedList<>();
        strs.add("a");
        strs.add("b");
        strs.add("c");
        strs.add("d");
        strs.add("e");
        strs.add("f");
        strs.remove("b");
        strs.remove("a");
        strs.remove("d");
        strs.remove("e");
        strs.remove("c");
        strs.remove("f");
        assertThat(strs.size()).isEqualTo(0);
    }

    // TODO

}
