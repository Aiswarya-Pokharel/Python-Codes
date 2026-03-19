class Node:
  def __init__(self,data):
    self.data= data
    self.next = None
  
class LinkedList:
  def __init__(self):
    self.head = None
  def add_song(self, song):
    new_node = Node(song)

    if not self.head:
      self.head = new_node
      return

    temp = self.head
    while temp.next:
      temp = temp.next

    temp.next = new_node

  def show_playlist(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next


playlist = LinkedList()
playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")
playlist.show_playlist()

