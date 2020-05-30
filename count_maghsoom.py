class Sol:
    def count_maghsoom(self,n):
        n=int(n)
        count=0
        sigma=0
        for i in range(1,n+1):
            for j in range(1,i+1):
                if i % j == 0:
                    count += 1
                    sigma +=j
        return f'{count} {sigma}'
