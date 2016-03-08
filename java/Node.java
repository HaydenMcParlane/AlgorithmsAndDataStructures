/*
*	Graph nodes for use in java data structures
*	@author: Hayden McParlane
*/
public class Node {
	Node parent = null;
	Node left = null;
	Node right = null;
	Integer key = null;

	public Node(Integer key){
		this.setKey(key);
		System.out.println("Key set to : " + key.toString());
	}

	public Integer getKey(){
		return this.key;
	}
	public void setKey(Integer key){
		this.key = key;
	}
	
	public Node getRight(){
		return this.right;
	}
	public void setRight(Node right){
		this.right = right;
	}

	public Node getLeft(){
		return this.left;
	}
	public void setLeft(Node left){
		this.left = left;
	}

	public Node getParent(){
		return this.parent;
	}
	public void setParent(Node parent){
		this.parent = parent;
	}

	public static void main(String[] args){
		System.out.println("Node successful");
	}
}
