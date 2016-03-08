/*
 * Binary Search Tree implementation using java
*/

public class BinarySearchTree {
	Node root = null;

	public void insert(Integer key, Node node){
		if (this.getRoot() == null){
			Node newNode = new Node(key);
			this.setRoot(newNode);
		}else{
			if( key <= node.getKey() ){
				if( node.getLeft() != null ){
					this.insert(key, node.getLeft());
				}else{
					Node newNode = new Node(key);
					newNode.setParent(node);
					node.setLeft(newNode);
					System.out.println("Added new node Left -> " + key);
				}
			}else if( key > node.getKey() ){
				if( node.getRight() != null){
					this.insert(key, node.getRight());
				}else{
					Node newNode = new Node(key);
					newNode.setParent(node);
					node.setRight(newNode);
					System.out.println("Added new node Right -> " + key);
				}
			}
		}
	}

	public void printValues(Node node){
		if( node == null ){
			node = this.getRoot();
			System.out.println("Node is now -> " + node.getKey().toString());
		}
		if( node.getLeft() != null )
			this.printValues(node.getLeft());
		System.out.println(node.getKey() + "\n");
		if( node.getRight() != null )
			this.printValues(node.getRight());
	}

	public Boolean search(){
		Boolean found = false;
		return found;
	}

	public Node getRoot(){
		return this.root;
	}
	public void setRoot(Node node){
		this.root = node;
	}

	public static void main(String[] args){
		System.out.println("Inserting test data\n");
		
		BinarySearchTree tree = new BinarySearchTree();

		tree.insert(100, tree.getRoot());
		tree.insert(34, tree.getRoot());
		tree.insert(120, tree.getRoot());
		tree.insert(34, tree.getRoot());
		tree.insert(55, tree.getRoot());
		tree.insert(334, tree.getRoot());
		tree.insert(500, tree.getRoot());
		tree.insert(45, tree.getRoot());
		tree.insert(14, tree.getRoot());
		tree.insert(232, tree.getRoot());
		tree.insert(222, tree.getRoot());

		tree.printValues(null);

		System.out.println("Binary Search Tree successful\n");
	}
}
