class CircularList:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyList:
    def __init__(self):
        self.start = None

    def endinsert(self, value):
        newone = CircularList(value)

        if self.start is None:
            newone.next = newone
            newone.prev = newone
            self.start = newone
        else:
            last = self.start.prev
            last.next = newone
            newone.prev.next = last
            newone.next = self.start
            self.start.prev = newone

    def insertbeginning(self, data):
        self.endinsert(data)
        self.start = self.start.prev

    def removing(self, value):
        if self.start is None:
            print("The list is empty")
            return
        current = self.start
        while True:
            if current.value == value:
                    if current.next == current:
                        self.start = None
                    else:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                        if current == self.start:
                            self.start = current.next
                        return
                    current = current.next
                    if current == self.start:
                        print("Value not found")
                        break

    def showlistforward(self):
        if self.start is None:
            print("The list is empty")
            return
        current = self.start
        values = []
        while True:
            values.append(str(current.value))
            current = current.next
            if current == self.start:
                break
        output_string = " -> ".join(values)
        print(output_string)

    def showbacklist(self):
        if self.start is None:
            print("The list is empty")
            return

        last = self.start.prev
        current = last
        values = []
        while True:
            values.append(str(current.value))
            current = current.prev
            if current == last:
                break
        output_string = " <- ".join(values)
        print(output_string)

if __name__ == '__main__':
    mycircle = CircularDoublyList()
    mycircle.endinsert("Quick")
    mycircle.endinsert("Brown")
    mycircle.endinsert("Fox")

    print("List after end insertion")
    mycircle.showlistforward()

    mycircle.insertbeginning("The")
    print("List after inserting at the beginning:")
    mycircle.showlistforward()

    print("Shown backlist")
    mycircle.showbacklist()

    mycircle.removing("Quick")
    print("List after removing QUICK:")
    mycircle.showlistforward()

    mycircle.removing("Quick")
    mycircle.removing("Slow")

    mycircle.removing("Brown")
    print("List after removing BROWN:")
    mycircle.showlistforward()

    mycircle.removing("The")
    mycircle.removing("Fox")
    print("List after removing all")

    mycircle.showlistforward()

