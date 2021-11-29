#ifndef _pnode_h
#define _pnode_h

typedef struct _pnode pNode;
typedef pNode pNodesList;

#include "defs.h"
#include "node.h"

struct _pnode{

  Node *n;
  
  pNode *prev;
  pNode *next;
};

pNode *createpNode(Node *n);
#endif

