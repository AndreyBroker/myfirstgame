def colision_detection(object1 : object, object2: object):

    # if type(object1) != object or type(object2) != object:
    #     raise TypeError("The parameters must be objects.")

    if object1.rect.x == object2.rect.x and object1.rect.y == object2.rect.y:
        return True
    else:
        return False

