from treelib import Tree


def create_family_tree():
    ## Create the player 1 tree
    tree = Tree()
    tree.create_node("Player 1", "P1")  # root node
    n_actions = input("Enter number of actions to player 1  ")
    n_actions=int(n_actions)
    for i in range(n_actions):
        p1_action1 = input("Enter utility of action 1 for player 1 ")
        p_id = "p1_" + str(i+1)
        tree.create_node(p1_action1,p_id, parent="P1")
    ## player 2
    m_actions = input("Enter number of actions to player 2 ")
    m_actions = int(m_actions)
    for i in range (n_actions):
        p_id="p2_"+str(i+1)
        parent_id= "p1_"+ str(i+1)
        tree.create_node("Player 2",p_id ,parent=parent_id)
        parent_id = p_id
        for j in range(m_actions):
            p2_action1 = input("Enter utility of action for player 2 ")
            p_id=parent_id+str(j+1)
            tree.create_node(p2_action1,p_id, parent=parent_id)
    ## player 3
    k_actions = input("Enter number of actions to player 3 ")
    k_actions = int(k_actions)
    for l in range(n_actions):
        for i in range(m_actions):
           p_id = "p3_"+ str(l + 1) +str(i+1)
           parent_id = "p2_" + str(l + 1)+ str(i + 1)
           tree.create_node("Player 3", p_id, parent=parent_id)
           parent_id = p_id
           for j in range(k_actions):
              p3_action1 = input("Enter utility of action for player 3 ")
              p_id = parent_id + str(j + 1)
              tree.create_node(p3_action1, p_id, parent=parent_id)
    return tree,n_actions,m_actions,k_actions

def delete_node(tree,k_actions,payoff,p_id):
    maxi = max(payoff)
    maxi_idx=payoff.index(maxi)
    for i in range(k_actions):
        if (i==maxi_idx):
            continue
        else:
            if(p_id=="P1"):
                p_id="p1_"
                deleted_id = p_id+ str(i + 1)
                tree.remove_node(deleted_id)
            else:
               deleted_id=p_id+str(i+1)
               tree.remove_node(deleted_id)
    return tree


def backward_induction(tree,n_actions,m_actions,k_actions):
   #player 3
   for i in range(n_actions):
       for j in range(m_actions):
           p_id="p3_"+str(i+1)+str(j+1)
           payoff=[]
           for child in tree.is_branch(p_id):
               payoff.append(tree[child].tag)
           tree=delete_node(tree,k_actions,payoff,p_id)
   tree.show()
   #player 2
   for j in range(n_actions):
       p_id = "p2_" +str(j + 1)
       payoff = []
       for child in tree.is_branch(p_id):
           payoff.append(tree[child].tag)
       tree = delete_node(tree, m_actions, payoff, p_id)
   tree.show()
   #player 1
   for j in range(1):
       p_id = "P1"
       payoff = []
       for child in tree.is_branch(p_id):
           payoff.append(tree[child].tag)
       tree = delete_node(tree,n_actions, payoff, p_id)
   tree.show()
   return tree


if __name__ == '__main__':
    tree,n_actions,m_actions,k_actions = create_family_tree()
    tree.show()
    backward_induction(tree,n_actions,m_actions,k_actions)

