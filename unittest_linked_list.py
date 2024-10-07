# Author: Paula Farebrother
# Created: July 2024
# Last modified: Oct 2024

from unittest import TestCase
from linked_list import LinkedList
from unittest.mock import patch, call


class TestLinkedList(TestCase):
    def setUp(self):
        self.llist = LinkedList()
        self.llist.append("TestPerson1")
        self.llist.append("TestPerson2")
        self.llist.append("TestPerson3")
        self.llist.append("TestPerson4")
        self.llist.append("TestPerson5")
        self.llist2 = LinkedList()
        self.llist2.append(1)
        self.llist2.append(2)
        self.llist2.append(3)
        self.llist2.append(4)

    def test_append_str(self):
        self.assertEqual(self.llist.head.data, "TestPerson1")
        self.assertEqual(self.llist.head.next.data, "TestPerson2")

    def test_append_num(self):
        self.assertEqual(self.llist2.head.data, 1)
        self.assertEqual(self.llist2.head.next.data, 2)

    @patch('builtins.print')  # Not sure if this is the best way to solve this?
    def test_print_list(self, mock_print):
        self.llist.printList()
        calls = [call(f"TestPerson{i+1}") for i in range(5)]
        mock_print.assert_has_calls(calls)


    def test_search(self):
        target1 = "TestPerson3"
        self.assertTrue(self.llist.search(target1))
        target2 = "TestPerson10"
        self.assertFalse(self.llist.search(target2))

    def test_count(self):
        expected_count = 5
        self.assertEqual(self.llist.count(), expected_count)

    def test_delete_head(self):
        newHead = self.llist.deleteHead()
        self.assertEqual(self.llist.head.data, "TestPerson2")

    def tearDown(self):
        pass

