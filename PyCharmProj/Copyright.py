'''
The program helps the user know if he/she could use the copyrighted image
'''

createImage = input('Did you take or create the image yourself? (yes or no): ')
if createImage == 'yes':
    originalIdea = input('Was the picture you created an original idea? (yes or no): ')
    if originalIdea == 'yes':
        print('YES! You are allowed to use the picture freely, '
              'since you own all copyrights to it.')
    elif originalIdea == 'no':
        print('NO! You are not allowed to use the picture '
              'for anything other than personal use.')

elif createImage == 'no':
    purpose = input('Are you using the image for personal, non-profit, '
                    'educational, research, or scholarly purposes AND '
                    'are you using the image sparingly, only for limited '
                    'purposes? (yes or no): ')
    if purpose == 'yes':
        print('YES! You are allowed to use the picture for educational purpose '
              'and non-profit uses.')
    elif purpose == 'no':
        newPurpse = input('Are you transforming or repurposing the image to create'
                          ' a new purpse or meaning? (yes or no): ')
        if newPurpse == 'yes':
            print('YES! You are allowed to use the picture if you completely '
                  'reworked it to an extent that it is not recognizeable from the original.')
        elif newPurpse == 'no':
            publish = input('Are you publishing the image in a fact-based context or'
                            ' publication that benefits the public as a whole? (yes or no): ')
            if publish == 'yes':
                print('PROBABLY. You are allowed to use the picture only if the image is '
                      'published in a non-biased way and to educate the public for good.')
            elif publish == 'no':
                possiblility = input('Would it be considered impossible to obtain '
                                     'permission form the original source? (yes or no): ')
                if possiblility == 'yes':
                    print('YES! You are allowed to use the image if permission is impossible'
                          ' to be obtained from the person who owns the credit.')
                elif possiblility == 'no':
                    gain = input('Will you be using the image for personal or commercial gain? (yes or no): ')
                    if gain == 'yes':
                        publicDomain = input('Is the image in the public domain or protected by creative '
                                             'commons agreements? (yes or no): ')
                        if publicDomain == 'yes':
                            print('YES! You are allowed to use the picture, since it is in the public '
                                  'domain, or if it is protected under creative commons.')
                        elif publicDomain == 'no':
                            purchase = input('Did you purchase the image or obtain permission from the '
                                             'original source? (yes or no): ')
                            if purchase == 'yes':
                                print('YES! You are allowed to use the picture, since you purchased its copyright.')
                            elif purchase == 'no':
                                print('NO! You are not allowed to use the picture, it is illegal.')
                    elif gain == 'no':
                        print('NO! You are not allowed to use the picture, it is illegal.')
