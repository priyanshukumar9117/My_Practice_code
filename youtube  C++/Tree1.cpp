#include<iostream>
using namespace std;
 class Node{
    public:
    int data;
    Node* left;
    Node *right;
    Node(int val){
        this->data=val;
        this->left=NULL;
        this->right=NULL;
    }
 };

 Node *createTree(){
    cout<<"enter the value for node:"<<endl;
    int data;
    cin>>data;
    
    if(data==-1){
        return NULL;
    }

    Node *root=new Node(data);
    cout<<"left of node:"<<root->data<<endl;
    root->left=createTree();
    cout<<"right of node:"<<root->data<<endl;
    root->right=createTree();
    return root;
 }

 Node * Preorder(Node* root){
    if(root==NULL) return 0;
    cout<<root->data<<" ";
    Preorder(root->left);
    Preorder(root->right);
 }
 int main(){
    Node *root=createTree();
    cout<<root->data<<endl;
    Preorder(root);
    return 0;
 }