
def abc():
    abc = [
        {
          "ids": "674b089b0000000002018c8b,673aef430000000007032f8c,6745d71c00000000060152eb"
        },
        {
          "ids": "6739930a000000001a036c7e,6733478f000000001901b780,673dc17e000000000202cb6e"
        }
      ]
    
    result = [  elm['ids'] for elm in abc ]

    print(result)


    depth =  3
    array = list(range(depth))
    r = {
        "array": array,
        "depth": depth
    }    
    print(r)

if __name__ == '__main__':
    abc()    