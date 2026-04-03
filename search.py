# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
from typing import List

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    # Initialize the fringe (frontier) with the start state
    # Each element is a tuple: (state, actions_to_reach_state)
    fringe = util.Stack()
    start_state = problem.getStartState()
    fringe.push((start_state, []))
    
    # Track visited states to implement graph search
    visited = set()
    
    while not fringe.isEmpty():
        # Pop the deepest node from the fringe
        state, actions = fringe.pop()
        
        # Check if we've already visited this state
        if state in visited:
            continue
        
        # Mark state as visited
        visited.add(state)
        
        # Check if this is the goal state
        if problem.isGoalState(state):
            return actions
        
        # Expand the state by getting its successors
        for successor_state, action, step_cost in problem.getSuccessors(state):
            if successor_state not in visited:
                # Add successor to fringe with updated actions
                fringe.push((successor_state, actions + [action]))
    
    # No solution found
    return []

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    # Initialize the fringe (frontier) with the start state
    # Each element is a tuple: (state, actions_to_reach_state)
    fringe = util.Queue()
    start_state = problem.getStartState()
    fringe.push((start_state, []))
    
    # Track visited states to implement graph search
    visited = set()
    
    while not fringe.isEmpty():
        # Pop the shallowest node from the fringe
        state, actions = fringe.pop()
        
        # Check if we've already visited this state
        if state in visited:
            continue
        
        # Mark state as visited
        visited.add(state)
        
        # Check if this is the goal state
        if problem.isGoalState(state):
            return actions
        
        # Expand the state by getting its successors
        for successor_state, action, step_cost in problem.getSuccessors(state):
            if successor_state not in visited:
                # Add successor to fringe with updated actions
                fringe.push((successor_state, actions + [action]))
    
    # No solution found
    return []

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    # Initialize the fringe with the start state using a priority queue
    # Items are prioritized by their accumulated cost
    fringe = util.PriorityQueue()
    start_state = problem.getStartState()
    fringe.push((start_state, []), 0)  # (state, actions), priority=cost
    
    # Track visited states to implement graph search
    visited = set()
    
    while not fringe.isEmpty():
        # Pop the lowest cost node from the fringe
        state, actions = fringe.pop()
        
        # Check if we've already visited this state
        if state in visited:
            continue
        
        # Mark state as visited
        visited.add(state)
        
        # Check if this is the goal state
        if problem.isGoalState(state):
            return actions
        
        # Expand the state by getting its successors
        for successor_state, action, step_cost in problem.getSuccessors(state):
            if successor_state not in visited:
                # Build the new action sequence
                new_actions = actions + [action]
                # Calculate the total cost of the new path
                new_cost = problem.getCostOfActions(new_actions)
                # Add successor to fringe with its accumulated cost as priority
                fringe.push((successor_state, new_actions), new_cost)
    
    # No solution found
    return []

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
