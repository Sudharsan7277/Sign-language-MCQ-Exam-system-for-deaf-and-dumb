import cv2 as cv
import numpy as np

def persons_input(hand_coordinates):
    # Function to determine the recognized input based on hand coordinates

    def distance(x1, y1, x2, y2):
        distance = int((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1 / 2))
        return distance

    persons_input = ""

    # Consider pawn is Vertical
    hand_horz = False

    # Consider all fingers are Down
    thumbs_up = False
    index_up = False
    middle_up = False
    ring_up = False
    little_up = False

    # Here I am using Hand Coordinates(HC) values, which we got from video input.
    # With the help of HC values, I can determine whether the finger is UP or DOWN
    # In "hand_coordinates[12][1]", "12" is the index and "1" is X_coordinate (and "2" for Y_coordinate)
    # For more information, refer to the "HAND_CORD" image (to understand the HC)

    if distance(hand_coordinates[0][2], 0, hand_coordinates[12][2], 0) < distance(hand_coordinates[0][1], 0,
                                                                                  hand_coordinates[12][1], 0):
        hand_horz = True
    if distance(hand_coordinates[0][1], hand_coordinates[0][2], hand_coordinates[3][1], hand_coordinates[3][2]) < \
            distance(hand_coordinates[0][1], hand_coordinates[0][2], hand_coordinates[4][1], hand_coordinates[4][2]):
        thumbs_up = True
    if distance(hand_coordinates[0][1], hand_coordinates[0][2], hand_coordinates[6][1], hand_coordinates[6][2]) < \
            distance(hand_coordinates[0][1], hand_coordinates[0][2], hand_coordinates[8][1], hand_coordinates[8][2]):
        index_up = True
    if distance(hand_coordinates[0][1], hand_coordinates[0][2], hand_coordinates[10][1], hand_coordinates[10][2]) < \
            distance(hand_coordinates[0][1], hand_coordinates[0][2], hand_coordinates[12][1],
                     hand_coordinates[12][2]):
        middle_up = True
    if distance(hand_coordinates[0][1], hand_coordinates[0][2], hand_coordinates[14][1], hand_coordinates[14][2]) < \
            distance(hand_coordinates[0][1], hand_coordinates[0][2], hand_coordinates[16][1],
                     hand_coordinates[16][2]):
        ring_up = True
    if distance(hand_coordinates[0][1], hand_coordinates[0][2], hand_coordinates[18][1], hand_coordinates[18][2]) < \
            distance(hand_coordinates[0][1], hand_coordinates[0][2], hand_coordinates[20][1],
                     hand_coordinates[20][2]):
        little_up = True

    # Get persons_input according to HC values

    if index_up == False and middle_up == False and ring_up == False and little_up == False and thumbs_up == True and \
            hand_horz == False:
        if distance(hand_coordinates[4][1], hand_coordinates[4][2], hand_coordinates[16][1],
                    hand_coordinates[16][2]) < distance(hand_coordinates[4][1], hand_coordinates[4][2],
                                                        hand_coordinates[13][1], hand_coordinates[13][2]):
            persons_input = " O"
        elif distance(hand_coordinates[4][1], hand_coordinates[4][2], hand_coordinates[18][1],
                      hand_coordinates[18][2]) < distance(hand_coordinates[14][1], hand_coordinates[14][2],
                                                          hand_coordinates[18][1], hand_coordinates[18][2]):
            persons_input = " M"
        elif distance(hand_coordinates[4][1], hand_coordinates[4][2], hand_coordinates[18][1],
                      hand_coordinates[18][2]) < distance(hand_coordinates[10][1], hand_coordinates[10][2],
                                                          hand_coordinates[18][1], hand_coordinates[18][2]):
            persons_input = " N"
        elif distance(hand_coordinates[4][1], hand_coordinates[4][2], hand_coordinates[18][1],
                      hand_coordinates[18][2]) < distance(hand_coordinates[6][1], hand_coordinates[6][2],
                                                          hand_coordinates[18][1], hand_coordinates[18][2]):
            persons_input = " T"
        else:
            persons_input = " A"
    elif index_up == True and middle_up == True and ring_up == True and little_up == True and thumbs_up == True and \
            hand_horz == False:
        if distance(hand_coordinates[4][1], hand_coordinates[4][2], hand_coordinates[12][1],
                    hand_coordinates[12][2]) < distance(hand_coordinates[4][1], hand_coordinates[4][2],
                                                        hand_coordinates[11][1], hand_coordinates[11][2]):
            persons_input = " C"
        elif distance(hand_coordinates[4][1], hand_coordinates[4][2], hand_coordinates[17][1],
                      hand_coordinates[17][2]) < distance(hand_coordinates[4][1], hand_coordinates[4][2],
                                                          hand_coordinates[5][1], hand_coordinates[5][2]):
            persons_input = " B"
    elif index_up == False and middle_up == False and ring_up == False and little_up == False and thumbs_up == False and \
            hand_horz == False:
        if distance(hand_coordinates[20][1], hand_coordinates[20][2], hand_coordinates[4][1],
                    hand_coordinates[4][2]) < distance(hand_coordinates[19][1], hand_coordinates[19][2],
                                                       hand_coordinates[4][1], hand_coordinates[4][2]):
            persons_input = " E"
        else:
            persons_input = " S"
    elif index_up == False and middle_up == True and ring_up == True and little_up == True and thumbs_up == True and \
            hand_horz == False:
        persons_input = " F"
    elif index_up == True and middle_up == False and ring_up == False and little_up == False and thumbs_up == True and \
            hand_horz == True:
        if distance(hand_coordinates[8][1], hand_coordinates[8][2], hand_coordinates[4][1],
                    hand_coordinates[4][2]) < distance(hand_coordinates[6][1], hand_coordinates[6][2],
                                                       hand_coordinates[4][1], hand_coordinates[4][2]):
            persons_input = " Q"
        elif distance(hand_coordinates[12][1], hand_coordinates[12][2], hand_coordinates[4][1],
                      hand_coordinates[4][2]) < distance(hand_coordinates[10][1], hand_coordinates[10][2],
                                                         hand_coordinates[4][1], hand_coordinates[4][2]):
            persons_input = " P"
        else:
            persons_input = " G"
    elif index_up == True and middle_up == True and ring_up == False and little_up == False and thumbs_up == True and \
            hand_horz == True:
        if distance(hand_coordinates[12][1], hand_coordinates[12][2], hand_coordinates[4][1],
                    hand_coordinates[4][2]) < distance(hand_coordinates[10][1], hand_coordinates[10][2],
                                                       hand_coordinates[4][1], hand_coordinates[4][2]):
            persons_input = " P"
        else:
            persons_input = " H"
    elif index_up == False and middle_up == False and ring_up == False and little_up == True and thumbs_up == False and \
            hand_horz == False:
        persons_input = " I"
    elif index_up == False and middle_up == False and ring_up == False and little_up == True and thumbs_up == False and \
            hand_horz == True:
        persons_input = " J"
    elif index_up == True and middle_up == True and ring_up == False and little_up == False and thumbs_up == True and \
            hand_horz == False:
        if hand_coordinates[8][1] < hand_coordinates[12][1]:
            persons_input = " R"
        elif distance(hand_coordinates[4][1], hand_coordinates[4][2], hand_coordinates[14][1],
                      hand_coordinates[14][2]) < distance(hand_coordinates[9][1], hand_coordinates[9][2],
                                                          hand_coordinates[14][1], hand_coordinates[14][2]):
            if 2 * distance(hand_coordinates[5][1], hand_coordinates[5][2], hand_coordinates[9][1],
                            hand_coordinates[9][2]) < distance(hand_coordinates[8][1], hand_coordinates[8][2],
                                                               hand_coordinates[12][1],
                                                               hand_coordinates[12][2]):
                persons_input = " V"
            else:
                persons_input = " U"
        elif distance(hand_coordinates[4][1], hand_coordinates[4][2], hand_coordinates[14][1],
                      hand_coordinates[14][2]) < distance(hand_coordinates[5][1], hand_coordinates[5][2],
                                                          hand_coordinates[14][1], hand_coordinates[14][2]):
            persons_input = " K"
    elif index_up == True and middle_up == False and ring_up == False and little_up == False and thumbs_up == True and \
            hand_horz == False:
        if distance(hand_coordinates[3][1], hand_coordinates[3][2], hand_coordinates[14][1],
                    hand_coordinates[14][2]) < distance(hand_coordinates[14][1], hand_coordinates[14][2],
                                                        hand_coordinates[4][1], hand_coordinates[4][2]):
            persons_input = " L"
        elif distance(hand_coordinates[8][1], hand_coordinates[8][2], hand_coordinates[10][1],
                      hand_coordinates[10][2]) < distance(hand_coordinates[6][1], hand_coordinates[6][2],
                                                          hand_coordinates[10][1], hand_coordinates[10][2]):
            persons_input = " X"
        else:
            persons_input = " D"
    elif index_up == True and middle_up == True and ring_up == False and little_up == False and thumbs_up == False and \
            hand_horz == False:
        if hand_coordinates[8][1] < hand_coordinates[12][1]:
            persons_input = " R"
        elif 2 * distance(hand_coordinates[5][1], hand_coordinates[5][2], hand_coordinates[9][1],
                          hand_coordinates[9][2]) < distance(hand_coordinates[8][1], hand_coordinates[8][2],
                                                             hand_coordinates[12][1],
                                                             hand_coordinates[12][2]):
            persons_input = " V"
        else:
            persons_input = " U"
    elif index_up == True and middle_up == True and ring_up == True and little_up == False and thumbs_up == True and \
            hand_horz == False:
        persons_input = " W"
    elif index_up == False and middle_up == False and ring_up == False and little_up == True and thumbs_up == True and \
            hand_horz == False:
        if distance(hand_coordinates[3][1], hand_coordinates[3][2], hand_coordinates[18][1],
                    hand_coordinates[18][2]) < distance(hand_coordinates[4][1], hand_coordinates[4][2],
                                                        hand_coordinates[18][1], hand_coordinates[18][2]):
            persons_input = " Y"
        else:
            persons_input = " I"

    return persons_input


def get_fram(image, hand_coordinate, string):
    # Function to draw a frame around the hand and display the recognized string
    def x_max(hand_coordinate):
        max_val = 0
        for coordinate_list in hand_coordinate:
            if max_val < coordinate_list[1]:  # 1 is x-coordinate value
                max_val = coordinate_list[1]
        return max_val

    def y_max(hand_coordinate):
        max_val = 0
        for coordinate_list in hand_coordinate:
            if max_val < coordinate_list[2]:  # 2 is y-coordinate value
                max_val = coordinate_list[2]
        return max_val

    def x_min(hand_coordinate):
        min_val = hand_coordinate[0][1]
        for coordinate_list in hand_coordinate:
            if min_val > coordinate_list[1]:
                min_val = coordinate_list[1]
        return min_val

    def y_min(hand_coordinate):
        min_val = hand_coordinate[0][2]
        for coordinate_list in hand_coordinate:
            if min_val > coordinate_list[2]:
                min_val = coordinate_list[2]
        return min_val

    def show_holy_rect(image, start_point, end_point, string):
        maxX = image.shape[1]
        # To create frame which contains hand
        image = cv.rectangle(image, start_point, end_point, (0, 0, 255), 1)
        # To create frame for letter
        image = cv.rectangle(image, (start_point[0], start_point[1] + 23), (end_point[0], start_point[1] + 3),
                             (0, 0, 255), -1)
        # Write letter in the frame
        image = cv.putText(cv.flip(image, 1), string, (maxX - end_point[0], start_point[1] + 20),
                           cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv.LINE_AA)
        return cv.flip(image, 1)

    image = show_holy_rect(image, (x_min(hand_coordinate) - 7, y_max(hand_coordinate) + 7),
                           (x_max(hand_coordinate) + 7, y_min(hand_coordinate) - 7), string)

    return image
