class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.height = 1

  def __init__(self):
    self.__root = None

  def __rinsert(self, value, t):
    if t is None:
      new_node = Binary_Search_Tree.__BST_Node(value)
      return new_node
    if t.value == value:
      raise ValueError
    if t.value > value:
      t.left = self.__rinsert(value, t.left)
      self.__check_height(t)
    if t.value < value:
      t.right = self.__rinsert(value, t.right)
      self.__check_height(t)
    return self.__balance(t)

  def __rremove(self, value, t):
    if t is None:
      raise ValueError
    elif t.value > value:
      t.left = self.__rremove(value, t.left)
      self.__check_height(t)
    elif t.value < value:
      t.right = self.__rremove(value, t.right)
      self.__check_height(t)
    elif t.value == value:
      if self.__check_children(t) == 0:
        return None
      elif self.__check_children(t) == 1:
        if t.left is None:
          return t.right
        else:
          return t.left
      elif self.__check_children(t) == 2:
        t.value = (self.__check_lowest(t.right))
        t.right = self.__rremove(t.value, t.right)
        self.__check_height(t)
    return self.__balance(t)

  def __check_lowest(self, t):
    if self.__check_children(t) == 0:
      return t.value
    else:
      if t.left is not None:
        current = t.left
        while current.left is not None:
          current = current.left
        return current.value
      else:
        return t.value

  def __check_children(self, t):
    if t.left is None and t.right is None:
      return 0
    elif t.left is not None and t.right is None:
      return 1
    elif t.right is not None and t.left is None:
      return 1
    elif t.left is not None and t.right is not None:
      return 2

  def insert_element(self, value):
    self.__root = self.__rinsert(value, self.__root)

  def remove_element(self, value):
    if self.__root is None:
      raise ValueError
    else:
      self.__root = self.__rremove(value, self.__root)

  def in_order(self):
    if self.__root is None:
      return '[ ]'
    else:
      string = '[ ' + self.__r_inorder(self.__root) + ']'
      string = string[:-3] + string[-2:]
      return string

  def __r_inorder(self, child):
    string = ''
    if child is not None:
      string = string + self.__r_inorder(child.left)
      string = string + str(child.value) + ', '
      string = string + self.__r_inorder(child.right) 
    return string

  def pre_order(self):
    if self.__root is None:
      return '[ ]'
    else:
      string = '[ ' + self.__r_preorder(self.__root) + ']'
      string = string[:-3] + string[-2:]
      return string

  def __r_preorder(self, child):
    string = ''
    if child is not None:
      string = string + str(child.value) + ', '
      string = string + self.__r_preorder(child.left)
      string = string + self.__r_preorder(child.right)
    return string

  def post_order(self):
    if self.__root is None:
      return '[ ]'
    else:
      string = '[ ' + self.__r_postorder(self.__root) + ']'
      string = string[:-3] + string[-2:]
      return string

  def __r_postorder(self, child):
    string = ''
    if child is not None:
      string = string + self.__r_postorder(child.left)
      string = string + self.__r_postorder(child.right)
      string = string + str(child.value) + ', '
    return string 

  def __balance(self, t):
    if self.__check_balance(t) == 0 or self.__check_balance(t) == -1 or self.__check_balance(t) == 1:
      return t
    if self.__check_balance(t) == -2:
      return self.__rotate_right(t)
    if self.__check_balance(t) == 2:
      return self.__rotate_left(t)
    
    # takes a node t as a parameter and treats it as the root of subtree. If the subtree rooted at t is 
    # unbalanced, rotate as necessary to balance it and return the new root of the now
    # balanced subtree. this balance operation will be invoked on the return path
    # from recursive insertion and removal,

  def __check_balance(self, t):
    if self.__check_children(t) == 0:
      return 0
    elif self.__check_children(t) == 1:
      if t.right == None:
        balance = 0 - t.left.height 
      if t.left == None:
        balance = t.right.height
    elif self.__check_children(t) == 2:
      balance = t.right.height - t.left.height
    return balance

  def __rotate_left(self, t):
    if self.__check_balance(t) > 0 and self.__check_balance(t.right) >= 0:
      old = t
      floater = t.right.left
      new_root = t.right
      new_root.left = old
      new_root.left.right = floater
      self.__check_height(old)
      self.__check_height(new_root)
      return new_root
    if self.__check_balance(t) > 0 and self.__check_balance(t.right) < 0:
      t.right = self.__pre_rotate_right(t.right)
      return self.__rotate_left(t)

    
  def __rotate_right(self, t):
    if self.__check_balance(t) < 0 and self.__check_balance(t.left) <= 0:
      old = t
      floater = t.left.right
      new_root = t.left
      new_root.right = old
      new_root.right.left = floater
      self.__check_height(old)
      self.__check_height(new_root)
      return new_root
    if self.__check_balance(t) < 0 and self.__check_balance(t.left) > 0:
      t.left = self.__pre_rotate_left(t.left)
      return self.__rotate_right(t)

  def __pre_rotate_left(self, t):
    old = t
    new_root = t.right
    floater = t.right.left
    new_root.left = old
    old.right = floater
    self.__check_height(old)
    self.__check_height(new_root)
    return new_root

  def __pre_rotate_right(self, t):
    old = t
    new_root = t.left
    floater = t.left.right
    new_root.right = old
    old.left = floater
    self.__check_height(old)
    self.__check_height(new_root)
    return new_root

  def __check_height(self, t):
    if t.right is None and t.left is None:
      t.height = 1
    if t.right is not None and t.left is None:
      t.height = t.right.height + 1
    if t.right is None and t.left is not None:
      t.height = t.left.height + 1
    if t.right is not None and t.left is not None:
      if t.right.height - t.left.height > 0:
        t.height = t.right.height + 1
      else:
        t.height = t.left.height + 1
    return t.height
  
  def get_height(self):
    if self.__root is None:
      return 0
    else:
      return self.__root.height

  def __str__(self):
    return self.in_order()

  def re_root(self):
      return self.__root

  def to_list(self):
    if self.__root is None:
      new_list = []
      return new_list
    else:
      new_list = self.__r_to_list(self.__root)
      return new_list

  def __r_to_list(self, child):
    old_list = []
    if child is not None:
      old_list = self.__r_to_list(child.left)
      old_list.append(child.value)
      old_list = old_list + self.__r_to_list(child.right)
    return old_list


  def print_tree(self, root, value="value", left="left", right="right"):
      def display(root, value=value, left=left, right=right):
          """Returns list of strings, width, height, and horizontal coordinate of the root."""
          # No child.
          if getattr(root, right) is None and getattr(root, left) is None:
              line = '%s' % getattr(root, value)
              width = len(line)
              height = 1
              middle = width // 2
              return [line], width, height, middle

          # Only left child.
          if getattr(root, right) is None:
              lines, n, p, x = display(getattr(root, left))
              s = '%s' % getattr(root, value)
              u = len(s)
              first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
              second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
              shifted_lines = [line + u * ' ' for line in lines]
              return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

          # Only right child.
          if getattr(root, left) is None:
              lines, n, p, x = display(getattr(root, right))
              s = '%s' % getattr(root, value)
              u = len(s)
              first_line = s + x * '_' + (n - x) * ' '
              second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
              shifted_lines = [u * ' ' + line for line in lines]
              return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

          # Two children.
          left, n, p, x = display(getattr(root, left))
          right, m, q, y = display(getattr(root, right))
          s = '%s' % getattr(root, value)
          u = len(s)
          first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
          second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
          if p < q:
              left += [n * ' '] * (q - p)
          elif q < p:
              right += [m * ' '] * (p - q)
          zipped_lines = zip(left, right)
          lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
          return lines, n + m + u, max(p, q) + 2, n + u // 2

      lines, *_ = display(root, value, left, right)
      for line in lines:
          print(line)

