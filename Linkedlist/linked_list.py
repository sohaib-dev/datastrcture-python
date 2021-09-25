class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:

    def __init__(self):
        self.head = None

    def get_nth_node(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            return self.head.data

        list_iterator = self.head
        count = 0
        indexed_data = None
        while list_iterator:
            count += 1
            list_iterator = list_iterator.next_node
            if count == index:
                indexed_data = list_iterator.data
                break
        return indexed_data

    def search_by_value(self, data_value):
        list_iterator = self.head
        is_data_present = False
        data_value_index = 0
        while list_iterator:
            if list_iterator.data == data_value:
                is_data_present = True
                break
            list_iterator = list_iterator.next_node
            data_value_index += 1
        if is_data_present:
            return data_value_index
        else:
            print(f'Searched data {data_value}, does not exist.')
            return

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return
        else:
            tmp = self.head
            while tmp.next_node:
                tmp = tmp.next_node

            tmp.next_node = Node(data, None)

    def insert_at_index(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        list_iterator = self.head
        count = 0
        while list_iterator:
            if count == index - 1:
                node = Node(data, list_iterator.next_node)
                list_iterator.next_node = node
                break
            count += 1
            list_iterator = list_iterator.next_node

    def insert_after_index(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        list_iterator = self.head
        count = 0
        while list_iterator:
            if count == index:
                node = Node(data, list_iterator.next_node)
                list_iterator.next_node = node
                break
            count += 1
            list_iterator = list_iterator.next_node

    def insert_after_value(self, data_after, data_to_inset):
        data_after_index = self.search_by_value(data_after)
        if data_after_index is None:
            raise Exception(f'Searched value does not exist')
        else:
            self.insert_after_index(data_after_index, data_to_inset)

    def list_to_linklist(self, data_values):
        if len(data_values) == 0:
            print("List is empty")
            return
        else:
            self.head = None
            for data in data_values:
                self.insert_at_end(data)

    def get_length(self):
        if self.head is None:
            return 0
        list_iterator = self.head
        count = 0
        while list_iterator:
            count += 1
            list_iterator = list_iterator.next_node
        return count

    def remove_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next_node
            return
        list_iterator = self.head
        count = 0
        while list_iterator:
            if count == index - 1:
                list_iterator.next_node = list_iterator.next_node.next_node
                break
            count += 1
            list_iterator = list_iterator.next_node

    def remove_by_value(self, data_value):
        if self.head.data == data_value:
            self.head = self.head.next_node
            return
        list_iterator = self.head
        previous_node = list_iterator
        is_data_present = False
        while list_iterator:
            if list_iterator.data == data_value:
                is_data_present = True
                previous_node.next_node = list_iterator.next_node
                list_iterator = None
                break
            previous_node = list_iterator
            list_iterator = list_iterator.next_node
        if not is_data_present:
            raise Exception(f'Given data {data_value}, does not exist.')
        else:
            return

    def print_linklist(self):
        if self.head is None:
            print("Linklist is empty.")
            return

        list_iterator = self.head
        list_str = ''

        while list_iterator:
            list_str += str(list_iterator.data) + ' --> '
            list_iterator = list_iterator.next_node
        print(list_str)


if __name__ == "__main__":

    linklist = LinkedList()
    linklist.list_to_linklist([1, 2, 3, 4])
    linklist.remove_by_value(2)

    linklist.print_linklist()

