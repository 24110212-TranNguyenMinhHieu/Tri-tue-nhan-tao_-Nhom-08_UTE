import flet as ft
import copy
import asyncio


def solve_bfs(matrix, winMatrix):
    father = None
    action = None
    step = 0
    fatherList = []
    actionList = []
    stepList = []
    matrixInFrontier = []
    frontier = [[matrix, father, action, step]]
    matrixInFrontier.append(frontier[0][0])
    reached = []
    done = False

    if matrix == winMatrix:
        return [matrix], ["None"], [0]

    while (not done and frontier):
        node, father, action, step = frontier.pop(0)
        matrixInFrontier.pop(0)
        reached.append(node)
        fatherList.append(father)
        actionList.append(action)
        stepList.append(step)

        for i in range(3):
            for j in range(3):
                if node[i][j] == 0:
                    x, y = i, j

        if x > 0:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x - 1][y]
            newMatrix[x - 1][y] = 0
            if newMatrix not in matrixInFrontier and newMatrix not in reached:
                if newMatrix == winMatrix:
                    reached.append(newMatrix)
                    fatherList.append(node)
                    actionList.append("UP")
                    stepList.append(step + 1)
                    done = True
                else:
                    frontier.append([newMatrix, node, "UP", step + 1])
                    matrixInFrontier.append(newMatrix)

        if not done and x < 2:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x + 1][y]
            newMatrix[x + 1][y] = 0
            if newMatrix not in matrixInFrontier and newMatrix not in reached:
                if newMatrix == winMatrix:
                    reached.append(newMatrix)
                    fatherList.append(node)
                    actionList.append("DOWN")
                    stepList.append(step + 1)
                    done = True
                else:
                    frontier.append([newMatrix, node, "DOWN", step + 1])
                    matrixInFrontier.append(newMatrix)

        if not done and y > 0:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x][y - 1]
            newMatrix[x][y - 1] = 0
            if newMatrix not in matrixInFrontier and newMatrix not in reached:
                if newMatrix == winMatrix:
                    reached.append(newMatrix)
                    fatherList.append(node)
                    actionList.append("LEFT")
                    stepList.append(step + 1)
                    done = True
                else:
                    frontier.append([newMatrix, node, "LEFT", step + 1])
                    matrixInFrontier.append(newMatrix)

        if not done and y < 2:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x][y + 1]
            newMatrix[x][y + 1] = 0
            if newMatrix not in matrixInFrontier and newMatrix not in reached:
                if newMatrix == winMatrix:
                    reached.append(newMatrix)
                    fatherList.append(node)
                    actionList.append("RIGHT")
                    stepList.append(step + 1)
                    done = True
                else:
                    frontier.append([newMatrix, node, "RIGHT", step + 1])
                    matrixInFrontier.append(newMatrix)

        if done:
            pathMatrix = []
            pathAction = []
            pathStep = []
            pathNode = reached[-1]

            while pathNode is not None:
                i = reached.index(pathNode)
                pathMatrix.append(reached[i])
                pathAction.append(actionList[i])
                pathStep.append(stepList[i])
                pathNode = fatherList[i]

            pathMatrix.reverse()
            pathAction.reverse()
            pathStep.reverse()

            return pathMatrix, pathAction, pathStep

    return None, None, None


def solve_dfs(matrix, winMatrix):
    father = None
    action = None
    step = 0
    fatherList = []
    actionList = []
    stepList = []
    matrixInFrontier = []
    frontier = [[matrix, father, action, step]]
    matrixInFrontier.append(frontier[0][0])
    reached = []
    done = False

    if matrix == winMatrix:
        return [matrix], ["None"], [0]

    while (not done and frontier):
        node, father, action, step = frontier.pop()
        if node in matrixInFrontier:
            matrixInFrontier.remove(node)

        reached.append(node)
        fatherList.append(father)
        actionList.append(action)
        stepList.append(step)

        for i in range(3):
            for j in range(3):
                if node[i][j] == 0:
                    x, y = i, j

        if x > 0:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x - 1][y]
            newMatrix[x - 1][y] = 0
            if newMatrix not in matrixInFrontier and newMatrix not in reached:
                if newMatrix == winMatrix:
                    reached.append(newMatrix)
                    fatherList.append(node)
                    actionList.append("UP")
                    stepList.append(step + 1)
                    done = True
                else:
                    frontier.append([newMatrix, node, "UP", step + 1])
                    matrixInFrontier.append(newMatrix)

        if not done and x < 2:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x + 1][y]
            newMatrix[x + 1][y] = 0
            if newMatrix not in matrixInFrontier and newMatrix not in reached:
                if newMatrix == winMatrix:
                    reached.append(newMatrix)
                    fatherList.append(node)
                    actionList.append("DOWN")
                    stepList.append(step + 1)
                    done = True
                else:
                    frontier.append([newMatrix, node, "DOWN", step + 1])
                    matrixInFrontier.append(newMatrix)

        if not done and y > 0:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x][y - 1]
            newMatrix[x][y - 1] = 0
            if newMatrix not in matrixInFrontier and newMatrix not in reached:
                if newMatrix == winMatrix:
                    reached.append(newMatrix)
                    fatherList.append(node)
                    actionList.append("LEFT")
                    stepList.append(step + 1)
                    done = True
                else:
                    frontier.append([newMatrix, node, "LEFT", step + 1])
                    matrixInFrontier.append(newMatrix)

        if not done and y < 2:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x][y + 1]
            newMatrix[x][y + 1] = 0
            if newMatrix not in matrixInFrontier and newMatrix not in reached:
                if newMatrix == winMatrix:
                    reached.append(newMatrix)
                    fatherList.append(node)
                    actionList.append("RIGHT")
                    stepList.append(step + 1)
                    done = True
                else:
                    frontier.append([newMatrix, node, "RIGHT", step + 1])
                    matrixInFrontier.append(newMatrix)

        if done:
            pathMatrix = []
            pathAction = []
            pathStep = []
            pathNode = reached[-1]

            while pathNode is not None:
                i = reached.index(pathNode)
                pathMatrix.append(reached[i])
                pathAction.append(actionList[i])
                pathStep.append(stepList[i])
                pathNode = fatherList[i]

            pathMatrix.reverse()
            pathAction.reverse()
            pathStep.reverse()

            return pathMatrix, pathAction, pathStep

    return None, None, None


def solve_ids(matrix, winMatrix, max_depth=30):
    done = False
    depth = 0

    while not done and depth <= max_depth:
        father = None
        action = None
        step = 0

        fatherList = []
        actionList = []
        stepList = []
        matrixInFrontier = []

        frontier = [[matrix, father, action, step]]
        matrixInFrontier.append(matrix)

        reached = []
        result = None

        while frontier:
            node, father, action, step = frontier.pop()
            if node in matrixInFrontier:
                matrixInFrontier.remove(node)

            reached.append(node)
            fatherList.append(father)
            actionList.append(action)
            stepList.append(step)

            if node == winMatrix:
                result = (reached, fatherList, actionList, stepList)
                break

            if step >= depth:
                continue

            for i in range(3):
                for j in range(3):
                    if node[i][j] == 0:
                        x, y = i, j

            children = []

            if x > 0:
                newMatrix = copy.deepcopy(node)
                newMatrix[x][y] = newMatrix[x - 1][y]
                newMatrix[x - 1][y] = 0

                if newMatrix not in matrixInFrontier and newMatrix not in reached:
                    if newMatrix == winMatrix:
                        reached.append(newMatrix)
                        fatherList.append(node)
                        actionList.append("UP")
                        stepList.append(step + 1)
                        result = (reached, fatherList, actionList, stepList)
                        break
                    children.append([newMatrix, node, "UP", step + 1])

            if result is not None:
                break

            if x < 2:
                newMatrix = copy.deepcopy(node)
                newMatrix[x][y] = newMatrix[x + 1][y]
                newMatrix[x + 1][y] = 0

                if newMatrix not in matrixInFrontier and newMatrix not in reached:
                    if newMatrix == winMatrix:
                        reached.append(newMatrix)
                        fatherList.append(node)
                        actionList.append("DOWN")
                        stepList.append(step + 1)
                        result = (reached, fatherList, actionList, stepList)
                        break
                    children.append([newMatrix, node, "DOWN", step + 1])

            if result is not None:
                break

            if y > 0:
                newMatrix = copy.deepcopy(node)
                newMatrix[x][y] = newMatrix[x][y - 1]
                newMatrix[x][y - 1] = 0

                if newMatrix not in matrixInFrontier and newMatrix not in reached:
                    if newMatrix == winMatrix:
                        reached.append(newMatrix)
                        fatherList.append(node)
                        actionList.append("LEFT")
                        stepList.append(step + 1)
                        result = (reached, fatherList, actionList, stepList)
                        break
                    children.append([newMatrix, node, "LEFT", step + 1])

            if result is not None:
                break

            if y < 2:
                newMatrix = copy.deepcopy(node)
                newMatrix[x][y] = newMatrix[x][y + 1]
                newMatrix[x][y + 1] = 0

                if newMatrix not in matrixInFrontier and newMatrix not in reached:
                    if newMatrix == winMatrix:
                        reached.append(newMatrix)
                        fatherList.append(node)
                        actionList.append("RIGHT")
                        stepList.append(step + 1)
                        result = (reached, fatherList, actionList, stepList)
                        break
                    children.append([newMatrix, node, "RIGHT", step + 1])

            if result is not None:
                break

            for child in children:
                frontier.append(child)
                matrixInFrontier.append(child[0])

        if result is not None:
            reached, fatherList, actionList, stepList = result
            pathMatrix = []
            pathAction = []
            pathStep = []

            pathNode = reached[-1]

            while pathNode is not None:
                i = reached.index(pathNode)
                pathMatrix.append(reached[i])
                pathAction.append(actionList[i])
                pathStep.append(stepList[i])
                pathNode = fatherList[i]

            pathMatrix.reverse()
            pathAction.reverse()
            pathStep.reverse()

            return pathMatrix, pathAction, pathStep

        depth += 1

    return None, None, None


def solve_greedy(matrix, winMatrix):
    def costCalGreedy(thisMatrix, thisStep):
        gn = thisStep
        hn = 0
        x1 = x2 = y1 = y2 = 0
        for a in range(1, 9):
            for i in range(3):
                for j in range(3):
                    if thisMatrix[i][j] == a:
                        x1, y1 = i, j
            for i in range(3):
                for j in range(3):
                    if winMatrix[i][j] == a:
                        x2, y2 = i, j
            hn = hn + abs(x1 - x2) + abs(y1 - y2)
        return gn + hn

    father = None
    action = None
    step = 0
    cost = costCalGreedy(matrix, step)

    fatherList = []
    actionList = []
    stepList = []
    matrixInFrontier = []

    frontier = [[matrix, father, action, step, cost]]
    matrixInFrontier.append(frontier[0][0])
    reached = []
    done = False

    while (not done and frontier):
        minCostMatrix = 0
        minCost = frontier[0][4]
        for i in range(1, len(frontier)):
            currCost = frontier[i][4]
            if currCost < minCost:
                minCost = currCost
                minCostMatrix = i

        node, father, action, step, cost = frontier.pop(minCostMatrix)
        matrixInFrontier.remove(node)
        reached.append(node)
        fatherList.append(father)
        actionList.append(action)
        stepList.append(step)

        if node == winMatrix:
            pathMatrix = []
            pathAction = []
            pathStep = []
            pathNode = node

            while pathNode is not None:
                i = reached.index(pathNode)
                pathMatrix.append(reached[i])
                pathAction.append(actionList[i])
                pathStep.append(stepList[i])
                pathNode = fatherList[i]

            pathMatrix.reverse()
            pathAction.reverse()
            pathStep.reverse()
            return pathMatrix, pathAction, pathStep

        for i in range(3):
            for j in range(3):
                if node[i][j] == 0:
                    x, y = i, j

        if x > 0:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x - 1][y]
            newMatrix[x - 1][y] = 0
            if newMatrix not in matrixInFrontier and newMatrix not in reached:
                newMatrixCost = costCalGreedy(newMatrix, step + 1)
                frontier.append([newMatrix, node, "UP", step + 1, newMatrixCost])
                matrixInFrontier.append(newMatrix)

        if x < 2:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x + 1][y]
            newMatrix[x + 1][y] = 0
            if newMatrix not in matrixInFrontier and newMatrix not in reached:
                newMatrixCost = costCalGreedy(newMatrix, step + 1)
                frontier.append([newMatrix, node, "DOWN", step + 1, newMatrixCost])
                matrixInFrontier.append(newMatrix)

        if y > 0:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x][y - 1]
            newMatrix[x][y - 1] = 0
            if newMatrix not in matrixInFrontier and newMatrix not in reached:
                newMatrixCost = costCalGreedy(newMatrix, step + 1)
                frontier.append([newMatrix, node, "LEFT", step + 1, newMatrixCost])
                matrixInFrontier.append(newMatrix)

        if y < 2:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x][y + 1]
            newMatrix[x][y + 1] = 0
            if newMatrix not in matrixInFrontier and newMatrix not in reached:
                newMatrixCost = costCalGreedy(newMatrix, step + 1)
                frontier.append([newMatrix, node, "RIGHT", step + 1, newMatrixCost])
                matrixInFrontier.append(newMatrix)

    return None, None, None


def solve_ucs(matrix, winMatrix):
    def costCalUCS(thisMatrix, thisStep):
        gn = thisStep
        for i in range(3):
            for j in range(3):
                if thisMatrix[i][j] != 0 and thisMatrix[i][j] != winMatrix[i][j]:
                    gn += 1
        return gn

    father = None
    action = None
    step = 0
    cost = costCalUCS(matrix, step)

    fatherList = []
    actionList = []
    stepList = []
    matrixInFrontier = []

    frontier = [[matrix, father, action, step, cost]]
    matrixInFrontier.append(frontier[0][0])
    reached = []
    done = False

    while (not done and frontier):
        minCostMatrix = 0
        minCost = frontier[0][4]
        for i in range(1, len(frontier)):
            currCost = frontier[i][4]
            if currCost < minCost:
                minCost = currCost
                minCostMatrix = i

        node, father, action, step, cost = frontier.pop(minCostMatrix)
        matrixInFrontier.remove(node)
        reached.append(node)
        fatherList.append(father)
        actionList.append(action)
        stepList.append(step)

        fatherCost = cost

        if node == winMatrix:
            pathMatrix = []
            pathAction = []
            pathStep = []
            pathNode = node

            while pathNode is not None:
                i = reached.index(pathNode)
                pathMatrix.append(reached[i])
                pathAction.append(actionList[i])
                pathStep.append(stepList[i])
                pathNode = fatherList[i]

            pathMatrix.reverse()
            pathAction.reverse()
            pathStep.reverse()
            return pathMatrix, pathAction, pathStep

        for i in range(3):
            for j in range(3):
                if node[i][j] == 0:
                    x, y = i, j

        if x > 0:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x - 1][y]
            newMatrix[x - 1][y] = 0
            if newMatrix not in matrixInFrontier and newMatrix not in reached:
                newMatrixCost = costCalUCS(newMatrix, step + 1)
                frontier.append([newMatrix, node, "UP", step + 1, newMatrixCost + fatherCost])
                matrixInFrontier.append(newMatrix)

        if x < 2:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x + 1][y]
            newMatrix[x + 1][y] = 0
            if newMatrix not in matrixInFrontier and newMatrix not in reached:
                newMatrixCost = costCalUCS(newMatrix, step + 1)
                frontier.append([newMatrix, node, "DOWN", step + 1, newMatrixCost + fatherCost])
                matrixInFrontier.append(newMatrix)

        if y > 0:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x][y - 1]
            newMatrix[x][y - 1] = 0
            if newMatrix not in matrixInFrontier and newMatrix not in reached:
                newMatrixCost = costCalUCS(newMatrix, step + 1)
                frontier.append([newMatrix, node, "LEFT", step + 1, newMatrixCost + fatherCost])
                matrixInFrontier.append(newMatrix)

        if y < 2:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x][y + 1]
            newMatrix[x][y + 1] = 0
            if newMatrix not in matrixInFrontier and newMatrix not in reached:
                newMatrixCost = costCalUCS(newMatrix, step + 1)
                frontier.append([newMatrix, node, "RIGHT", step + 1, newMatrixCost + fatherCost])
                matrixInFrontier.append(newMatrix)

    return None, None, None


def solve_astar(matrix, winMatrix):
    def costCal(thisMatrix, thisStep):
        gn = thisStep
        hn = 0
        x1 = x2 = y1 = y2 = 0
        for a in range(1, 9):
            for i in range(3):
                for j in range(3):
                    if thisMatrix[i][j] == a:
                        x1, y1 = i, j
                    if winMatrix[i][j] == a:
                        x2, y2 = i, j
            hn = hn + abs(x1 - x2) + abs(y1 - y2)
        return gn + hn

    father = None
    action = None
    step = 0
    cost = costCal(matrix, step)

    costList = []
    fatherList = []
    actionList = []
    stepList = []
    matrixInFrontier = []

    frontier = [[matrix, father, action, step, cost]]
    matrixInFrontier.append(frontier[0][0])
    reached = []
    done = False

    while (not done and frontier):
        minCostMatrix = 0
        minCost = frontier[0][4]
        for i in range(1, len(frontier)):
            currCost = frontier[i][4]
            if currCost < minCost:
                minCost = currCost
                minCostMatrix = i

        node, father, action, step, cost = frontier.pop(minCostMatrix)
        matrixInFrontier.remove(node)
        reached.append(node)
        fatherList.append(father)
        actionList.append(action)
        stepList.append(step)
        costList.append(cost)

        if node == winMatrix:
            pathMatrix = []
            pathAction = []
            pathStep = []
            pathNode = node

            while pathNode is not None:
                i = reached.index(pathNode)
                pathMatrix.append(reached[i])
                pathAction.append(actionList[i])
                pathStep.append(stepList[i])
                pathNode = fatherList[i]

            pathMatrix.reverse()
            pathAction.reverse()
            pathStep.reverse()
            return pathMatrix, pathAction, pathStep

        for i in range(3):
            for j in range(3):
                if node[i][j] == 0:
                    x, y = i, j

        if x > 0:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x - 1][y]
            newMatrix[x - 1][y] = 0

            g_new = step + 1
            newMatrixCost = costCal(newMatrix, g_new)

            in_frontier = False
            in_reached = False

            for i in range(len(reached)):
                if reached[i] == newMatrix:
                    in_reached = True
                    if g_new < stepList[i]:
                        reached.pop(i)
                        fatherList.pop(i)
                        actionList.pop(i)
                        stepList.pop(i)
                        costList.pop(i)

                        frontier.append([newMatrix, node, "UP", g_new, newMatrixCost])
                        matrixInFrontier.append(newMatrix)
                    break

            if not in_reached:
                for i in range(len(frontier)):
                    if frontier[i][0] == newMatrix:
                        in_frontier = True
                        if g_new < frontier[i][3]:
                            frontier[i][1] = node
                            frontier[i][2] = "UP"
                            frontier[i][3] = g_new
                            frontier[i][4] = newMatrixCost
                        break

            if not in_reached and not in_frontier:
                frontier.append([newMatrix, node, "UP", g_new, newMatrixCost])
                matrixInFrontier.append(newMatrix)

        if x < 2:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x + 1][y]
            newMatrix[x + 1][y] = 0

            g_new = step + 1
            newMatrixCost = costCal(newMatrix, g_new)

            in_frontier = False
            in_reached = False

            for i in range(len(reached)):
                if reached[i] == newMatrix:
                    in_reached = True
                    if g_new < stepList[i]:
                        reached.pop(i)
                        fatherList.pop(i)
                        actionList.pop(i)
                        stepList.pop(i)
                        costList.pop(i)

                        frontier.append([newMatrix, node, "DOWN", g_new, newMatrixCost])
                        matrixInFrontier.append(newMatrix)
                    break

            if not in_reached:
                for i in range(len(frontier)):
                    if frontier[i][0] == newMatrix:
                        in_frontier = True
                        if g_new < frontier[i][3]:
                            frontier[i][1] = node
                            frontier[i][2] = "DOWN"
                            frontier[i][3] = g_new
                            frontier[i][4] = newMatrixCost
                        break

            if not in_reached and not in_frontier:
                frontier.append([newMatrix, node, "DOWN", g_new, newMatrixCost])
                matrixInFrontier.append(newMatrix)

        if y > 0:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x][y - 1]
            newMatrix[x][y - 1] = 0

            g_new = step + 1
            newMatrixCost = costCal(newMatrix, g_new)

            in_frontier = False
            in_reached = False

            for i in range(len(reached)):
                if reached[i] == newMatrix:
                    in_reached = True
                    if g_new < stepList[i]:
                        reached.pop(i)
                        fatherList.pop(i)
                        actionList.pop(i)
                        stepList.pop(i)
                        costList.pop(i)

                        frontier.append([newMatrix, node, "LEFT", g_new, newMatrixCost])
                        matrixInFrontier.append(newMatrix)
                    break

            if not in_reached:
                for i in range(len(frontier)):
                    if frontier[i][0] == newMatrix:
                        in_frontier = True
                        if g_new < frontier[i][3]:
                            frontier[i][1] = node
                            frontier[i][2] = "LEFT"
                            frontier[i][3] = g_new
                            frontier[i][4] = newMatrixCost
                        break

            if not in_reached and not in_frontier:
                frontier.append([newMatrix, node, "LEFT", g_new, newMatrixCost])
                matrixInFrontier.append(newMatrix)

        if y < 2:
            newMatrix = copy.deepcopy(node)
            newMatrix[x][y] = newMatrix[x][y + 1]
            newMatrix[x][y + 1] = 0

            g_new = step + 1
            newMatrixCost = costCal(newMatrix, g_new)

            in_frontier = False
            in_reached = False

            for i in range(len(reached)):
                if reached[i] == newMatrix:
                    in_reached = True
                    if g_new < stepList[i]:
                        reached.pop(i)
                        fatherList.pop(i)
                        actionList.pop(i)
                        stepList.pop(i)
                        costList.pop(i)

                        frontier.append([newMatrix, node, "RIGHT", g_new, newMatrixCost])
                        matrixInFrontier.append(newMatrix)
                    break

            if not in_reached:
                for i in range(len(frontier)):
                    if frontier[i][0] == newMatrix:
                        in_frontier = True
                        if g_new < frontier[i][3]:
                            frontier[i][1] = node
                            frontier[i][2] = "RIGHT"
                            frontier[i][3] = g_new
                            frontier[i][4] = newMatrixCost
                        break

            if not in_reached and not in_frontier:
                frontier.append([newMatrix, node, "RIGHT", g_new, newMatrixCost])
                matrixInFrontier.append(newMatrix)

    return None, None, None


def solve_idastar(matrix, winMatrix):
    def costCal(thisMatrix, thisStep):
        gn = thisStep
        hn = 0
        x1 = x2 = y1 = y2 = 0
        for a in range(1, 9):
            for i in range(3):
                for j in range(3):
                    if thisMatrix[i][j] == a:
                        x1, y1 = i, j
                    if winMatrix[i][j] == a:
                        x2, y2 = i, j
            hn = hn + abs(x1 - x2) + abs(y1 - y2)
        return gn + hn

    done = False
    costLimit = costCal(matrix, 0)

    while not done:
        father = None
        action = None
        step = 0

        fatherList = []
        actionList = []
        stepList = []
        matrixInFrontier = []

        frontier = [[matrix, father, action, step]]
        matrixInFrontier.append(matrix)

        reached = []
        result = None
        nextCostLimit = float('inf')

        while frontier:
            node, father, action, step = frontier.pop()
            if node in matrixInFrontier:
                matrixInFrontier.remove(node)

            reached.append(node)
            fatherList.append(father)
            actionList.append(action)
            stepList.append(step)

            if node == winMatrix:
                result = (reached, fatherList, actionList, stepList)
                break

            for i in range(3):
                for j in range(3):
                    if node[i][j] == 0:
                        x, y = i, j

            children = []

            if x > 0:
                newMatrix = copy.deepcopy(node)
                newMatrix[x][y] = newMatrix[x-1][y]
                newMatrix[x-1][y] = 0

                if newMatrix not in matrixInFrontier and newMatrix not in reached:
                    costChild = costCal(newMatrix, step + 1)
                    if costChild > costLimit:
                        if costChild < nextCostLimit:
                            nextCostLimit = costChild
                    else:
                        if newMatrix == winMatrix:
                            reached.append(newMatrix)
                            fatherList.append(node)
                            actionList.append("UP")
                            stepList.append(step + 1)
                            result = (reached, fatherList, actionList, stepList)
                            break
                        children.append([newMatrix, node, "UP", step + 1])

            if result is not None: break

            if x < 2:
                newMatrix = copy.deepcopy(node)
                newMatrix[x][y] = newMatrix[x+1][y]
                newMatrix[x+1][y] = 0

                if newMatrix not in matrixInFrontier and newMatrix not in reached:
                    costChild = costCal(newMatrix, step + 1)
                    if costChild > costLimit:
                        if costChild < nextCostLimit:
                            nextCostLimit = costChild
                    else:
                        if newMatrix == winMatrix:
                            reached.append(newMatrix)
                            fatherList.append(node)
                            actionList.append("DOWN")
                            stepList.append(step + 1)
                            result = (reached, fatherList, actionList, stepList)
                            break
                        children.append([newMatrix, node, "DOWN", step + 1])

            if result is not None: break

            if y > 0:
                newMatrix = copy.deepcopy(node)
                newMatrix[x][y] = newMatrix[x][y-1]
                newMatrix[x][y-1] = 0

                if newMatrix not in matrixInFrontier and newMatrix not in reached:
                    costChild = costCal(newMatrix, step + 1)
                    if costChild > costLimit:
                        if costChild < nextCostLimit:
                            nextCostLimit = costChild
                    else:
                        if newMatrix == winMatrix:
                            reached.append(newMatrix)
                            fatherList.append(node)
                            actionList.append("LEFT")
                            stepList.append(step + 1)
                            result = (reached, fatherList, actionList, stepList)
                            break
                        children.append([newMatrix, node, "LEFT", step + 1])

            if result is not None: break

            if y < 2:
                newMatrix = copy.deepcopy(node)
                newMatrix[x][y] = newMatrix[x][y+1]
                newMatrix[x][y+1] = 0

                if newMatrix not in matrixInFrontier and newMatrix not in reached:
                    costChild = costCal(newMatrix, step + 1)
                    if costChild > costLimit:
                        if costChild < nextCostLimit:
                            nextCostLimit = costChild
                    else:
                        if newMatrix == winMatrix:
                            reached.append(newMatrix)
                            fatherList.append(node)
                            actionList.append("RIGHT")
                            stepList.append(step + 1)
                            result = (reached, fatherList, actionList, stepList)
                            break
                        children.append([newMatrix, node, "RIGHT", step + 1])

            if result is not None: break

            for child in children:
                frontier.append(child)
                matrixInFrontier.append(child[0])

        if result is not None:
            reached, fatherList, actionList, stepList = result
            pathMatrix = []
            pathAction = []
            pathStep = []
            pathNode = reached[-1]

            while pathNode is not None:
                i = reached.index(pathNode)
                pathMatrix.append(reached[i])
                pathAction.append(actionList[i])
                pathStep.append(stepList[i])
                pathNode = fatherList[i]

            pathMatrix.reverse()
            pathAction.reverse()
            pathStep.reverse()
            return pathMatrix, pathAction, pathStep

        costLimit = nextCostLimit

    return None, None, None


def main(page: ft.Page):
    page.title = "8-Puzzle Multi-Algorithm Visualizer"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 900
    page.window.height = 850
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    input_field = ft.TextField(
        label="Nhập ma trận (ví dụ: 1 2 3 4 0 6 7 5 8)",
        value="1 2 3 4 0 6 7 5 8",
        width=350
    )

    algo_dropdown = ft.Dropdown(
        label="Thuật toán",
        options=[
            ft.dropdown.Option("BFS"),
            ft.dropdown.Option("DFS"),
            ft.dropdown.Option("IDS"),
            ft.dropdown.Option("Greedy"),
            ft.dropdown.Option("UCS"),
            ft.dropdown.Option("A*"),
            ft.dropdown.Option("IDA*"),
        ],
        value="BFS",
        width=150
    )

    log_view = ft.ListView(expand=True, spacing=5, padding=10)
    grid_container = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def create_puzzle_ui(matrix):
        rows = []
        for r in range(3):
            cols = []
            for c in range(3):
                val = matrix[r][c]
                cols.append(
                    ft.Container(
                        content=ft.Text(str(val) if val != 0 else "", size=25, weight="bold"),
                        alignment=ft.Alignment(0, 0),
                        width=70, height=70,
                        bgcolor=ft.Colors.BLUE_ACCENT_700 if val != 0 else ft.Colors.GREY_900,
                        border_radius=10,
                    )
                )
            rows.append(ft.Row(cols, alignment=ft.MainAxisAlignment.CENTER))
        return ft.Container(content=ft.Column(rows), padding=20)

    async def solve_and_animate(e):
        try:
            raw_data = list(map(int, input_field.value.split()))
            if len(raw_data) != 9:
                raise ValueError
            matrix = [raw_data[i:i + 3] for i in range(0, 9, 3)]
        except:
            log_view.controls.append(ft.Text("Lỗi: Nhập đúng 9 số nguyên cách nhau bằng khoảng trắng!", color="red"))
            page.update()
            return

        winMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        selected_algo = algo_dropdown.value

        log_view.controls.clear()
        log_view.controls.append(ft.Text(f"Đang tính toán bằng {selected_algo}...", color="yellow"))

        grid_container.controls.clear()
        grid_container.controls.append(ft.Text("BƯỚC: 0 | INIT", size=20))
        grid_container.controls.append(create_puzzle_ui(matrix))
        page.update()

        await asyncio.sleep(0.1)

        pathMatrix, pathAction, pathStep = None, None, None

        if selected_algo == "BFS":
            pathMatrix, pathAction, pathStep = solve_bfs(matrix, winMatrix)
        elif selected_algo == "DFS":
            pathMatrix, pathAction, pathStep = solve_dfs(matrix, winMatrix)
        elif selected_algo == "IDS":
            pathMatrix, pathAction, pathStep = solve_ids(matrix, winMatrix)
        elif selected_algo == "Greedy":
            pathMatrix, pathAction, pathStep = solve_greedy(matrix, winMatrix)
        elif selected_algo == "UCS":
            pathMatrix, pathAction, pathStep = solve_ucs(matrix, winMatrix)
        elif selected_algo == "A*":
            pathMatrix, pathAction, pathStep = solve_astar(matrix, winMatrix)
        elif selected_algo == "IDA*":
            pathMatrix, pathAction, pathStep = solve_idastar(matrix, winMatrix)

        if pathMatrix:
            log_view.controls.append(ft.Text(f"Tìm thấy đích sau {len(pathMatrix) - 1} bước!", color="green"))
            page.update()
            await asyncio.sleep(1)

            for i in range(len(pathMatrix)):
                grid_container.controls.clear()
                grid_container.controls.append(ft.Text(f"BƯỚC: {pathStep[i]} | {pathAction[i]}", size=20))
                grid_container.controls.append(create_puzzle_ui(pathMatrix[i]))
                log_view.controls.insert(0, ft.Text(f"Step {pathStep[i]}: {pathAction[i]}"))
                page.update()
                await asyncio.sleep(0.5)
        else:
            log_view.controls.append(ft.Text("Không tìm thấy kết quả hoặc đạt giới hạn duyệt!", color="red"))
            page.update()

    page.add(
        ft.Text("8-Puzzle Visualizer", size=30, weight="bold", color="blueaccent"),
        ft.Row([
            input_field,
            algo_dropdown,
            ft.FilledButton("Giải", icon=ft.Icons.PLAY_ARROW, on_click=solve_and_animate)
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(),
        ft.Row([
            ft.Container(grid_container, expand=2),
            ft.VerticalDivider(),
            ft.Container(
                content=ft.Column([ft.Text("Log:"), log_view]),
                expand=1, bgcolor=ft.Colors.WHITE10, padding=10, border_radius=10
            )
        ], height=500)
    )


if __name__ == "__main__":
    ft.run(main)