#ifndef _graph_h
#define _graph_h

#include "defs.h"
#include "nodesList.h"

typedef struct _graph Graph;

struct _graph{

  int numNodes;
  int numEdges;

  NodesList *nodesList;
};


Graph *createGraph(int numNodes,int numEdges);

void initNodes(int numNodes,Graph *g);

#endif
