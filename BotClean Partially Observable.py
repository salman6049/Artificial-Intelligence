# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 20:19:48 2020

@author: Salman
"""

import os


def get_right_move(botPosition, nextPosition):
    rightMove = None
    # Find the distance between the bot position and the next position
    x = botPosition[0] - nextPosition[0]
    y = botPosition[1] - nextPosition[1]

    if x == 0 and y == 0:
        rightMove = "CLEAN"
    elif abs(x) > abs(y):
        if x > 0:
            rightMove = "UP"
        else:
            rightMove = "DOWN"
    else:
        if y > 0:
            rightMove = "LEFT"
        else:
            rightMove = "RIGHT"

    return rightMove


def get_visible_points(position, move_dir):
    """
    Assumption here is that next move is correct and not out of bound
    """
    # Boundaries of the grid
    Xmin, Xmax, Ymin, Ymax = 0, 4, 0, 4
    newPosition = [0, 0]
    # Get the new position
    if move_dir == "UP":
        newPosition[0], newPosition[1] = position[0] - 1, position[1]
    elif move_dir == "DOWN":
        newPosition[0], newPosition[1] = position[0] + 1, position[1]
    elif move_dir == "LEFT":
        newPosition[0], newPosition[1] = position[0], position[1] - 1
    elif move_dir == "RIGHT":
        newPosition[0], newPosition[1] = position[0], position[1] + 1
    else:
        newPosition[0], newPosition[1] = position[0], position[1]

    # Deduce the visible points
    visiblePoints = []

    visiblePoints.append(
        [max(newPosition[0] - 1, Xmin), max(newPosition[1] - 1, Ymin)])
    visiblePoints.append(
        [max(newPosition[0] - 1, Xmin), newPosition[1]])
    visiblePoints.append(
        [max(newPosition[0] - 1, Xmin), min(newPosition[1] + 1, Ymax)])
    visiblePoints.append(
        [newPosition[0], max(newPosition[1] - 1, Ymin)])
    visiblePoints.append(
        [newPosition[0], newPosition[1]])
    visiblePoints.append(
        [newPosition[0], min(newPosition[1] + 1, Ymax)])
    visiblePoints.append(
        [min(newPosition[0] + 1, Xmax), max(newPosition[1] - 1, Ymin)])
    visiblePoints.append(
        [min(newPosition[0] + 1, Xmax), newPosition[1]])
    visiblePoints.append(
        [min(newPosition[0] + 1, Xmax), min(newPosition[1] + 1, Ymax)])

    # Return the visiblePoints list
    return visiblePoints


def next_move(posr, posc, board):
    # Get the bot position
    botPos = (posr, posc)
    oldDirtyPlaces = []
    unobsvSpotsList = []

    # Open the file to read dirty places from it
    fn = 'dirtyFile'
    if os.path.exists(fn):
        # Open in read mode
        fh = open(fn, "r")
        oldDirtyPlaces = fh.readlines()
        fh.close()

    # Read unobserved places from file
    fileName = 'unobserved'
    if os.path.exists(fileName):
        # Open in read mode
        fh = open(fn, "r")
        unobsvSpotsList = fh.readlines()
        fh.close()

    # Now scan the grid and find the nearest 'd' i.e. dirty position
    rowNum = 0
    nearestDirtyPos = None
    nearestDirtyDist = None

    # First read the old points in list
    for pos in oldDirtyPlaces:
        newPos = pos.replace("\n", "")
        dirtyPos = [int(pp) for pp in newPos.split(" ")]
        dist = abs(botPos[0] - dirtyPos[0]) + abs(botPos[1] - dirtyPos[1])
        if nearestDirtyDist is None or dist < nearestDirtyDist:
            nearestDirtyDist = dist
            nearestDirtyPos = dirtyPos

    for row in board:
        # Find the nearest dirty spot
        allPos = [i for i, x in enumerate(row) if x == 'd']
        for pos in allPos:
            dirtyPos = (rowNum, pos)
            # Add it to old dirty places
            strPos = str(dirtyPos[0]) + " " + str(dirtyPos[1]) + "\n"
            if strPos not in oldDirtyPlaces:
                oldDirtyPlaces.append(strPos)
            # Find manhattan distance with the current dirty position
            # and tag it as nearest if distance is less than previous
            # dirty distance
            dist = abs(botPos[0] - dirtyPos[0]) + abs(botPos[1] - dirtyPos[1])
            if nearestDirtyDist is None or dist < nearestDirtyDist:
                nearestDirtyDist = dist
                nearestDirtyPos = dirtyPos

        # Increment the row number
        rowNum += 1

    # Now find the next move
    retMove = None

    # Now return the right move
    if nearestDirtyDist is not None:
        # This means we have a dirty spot to clean
        # Remove it from old dirty places
        strPos = str(nearestDirtyPos[0]) + " " + str(nearestDirtyPos[1]) + "\n"
        if strPos in oldDirtyPlaces:
            oldDirtyPlaces.remove(strPos)

        # Get the direction to move
        retMove = get_right_move(botPos, nearestDirtyPos)

        # Remove all entries in unobserved list, we don't care about them for now
        unobsvSpotsList = []

    else:
        # This means we need to explore unobserved areas
        nearestUOpos = None
        nearestUOdist = None
        # Now check if unobsvSpotsList is empty or not
        if len(unobsvSpotsList) != 0:
            # This means we are still looking for a dirty place, so parse the
            # list and find nearest unobserved point to move towards
            for pos in unobsvSpotsList:
                newPos = pos.replace("\n", "")
                uoPos = [int(pp) for pp in newPos.split(" ")]
                dist = abs(botPos[0] - uoPos[0]) + abs(botPos[1] - uoPos[1])
                if nearestUOdist is None or dist < nearestUOdist:
                    nearestUOdist = dist
                    nearestUOpos = uoPos

            # Find the direction to move
            retMove = get_right_move(botPos, nearestUOpos)

            # Now find the points which have become visible
            visiblePoints = get_visible_points(botPos, retMove)

            # Remove visible points from the unobserved points list
            for pt in visiblePoints:
                strPt = str(pt[0]) + " " + str(pt[1]) + "\n"
                if strPt in unobsvSpotsList:
                    unobsvSpotsList.remove(strPt)

        else:
            # If there is no point in unobserved points list,
            # this means we have to construct the list from scratch
            rowNumber = 0
            for row in board:
                # Find the nearest dirty position
                unobsPos = [i for i, x in enumerate(row) if x == 'o']
                for pos in unobsPos:
                    uoPos = (rowNumber, pos)
                    # Add it to unobserved positions list
                    strUOpos = str(uoPos[0]) + " " + str(uoPos[1]) + "\n"
                    if strUOpos not in unobsvSpotsList:
                        unobsvSpotsList.append(strUOpos)
                    # Also keep track of nearest point
                    dist = abs(botPos[0] - uoPos[0]) + abs(botPos[1] - uoPos[1])
                    if nearestUOdist is None or dist < nearestUOdist:
                        nearestUOdist = dist
                        nearestUOpos = uoPos

                # Increment the row Number
                rowNumber += 1

            # Find the direction to move
            retMove = get_right_move(botPos, nearestUOpos)

            # Now find the points which have become visible
            visiblePoints = get_visible_points(botPos, retMove)

            # Remove visible points from the unobserved points list
            for pt in visiblePoints:
                strPt = str(pt[0]) + " " + str(pt[1]) + "\n"
                if strPt in unobsvSpotsList:
                    unobsvSpotsList.remove(strPt)


    # Open dirtyplaces file in write mode and write dirty places to it
    fh = open(fn, "w")
    fh.writelines(oldDirtyPlaces)
    fh.close()

    # Open unobserved places file in write mode
    fh2 = open(fileName, "w")
    fh2.writelines(unobsvSpotsList)
    fh2.close()

    # Print the move
    print retMove
    
    
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)