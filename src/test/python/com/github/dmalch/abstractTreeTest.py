class AbstractTreeTest(object):
    def getTree(self):
        pass

    def testTree(self):
        tree = self.getTree()
        expectedValue = "1"

        tree.put(1, expectedValue)

        self.assertEqual(tree.get(1), expectedValue)

    def testTree2(self):
        tree = self.getTree()
        tree.put(1, "1")
        tree.put(2, "2")

        self.assertEqual(tree.get(1), "1")
        self.assertEqual(tree.get(2), "2")

    def testTree3(self):
        tree = self.getTree()
        tree.put(2, "2")
        tree.put(1, "1")
        tree.put(3, "3")

        self.assertEqual(tree.get(1), "1")
        self.assertEqual(tree.get(2), "2")
        self.assertEqual(tree.get(3), "3")

    def testTree4(self):
        tree = self.getTree()
        tree.put(1, "1")
        tree.put(2, "2")
        tree.put(2, "3")

        self.assertEqual(tree.get(2), "3")
