import digitalocean
api = "SecretKeyHere"

drop = digitalocean.Droplet(
    token=api,
    name=input('Please enter a name for your droplet'),
    region='nyc3',
    image=input('Please enter a image name'),
    size='512mb',
    backups='false'
)

#Function1
def get_droplets():
    if api == "SecretKeyHere":
        dropletmanager = digitalocean.Manager(token=api)
        getdroplets = dropletmanager.get_all_droplets()
        print(getdroplets)

def new_droplet():
    createdroplet = input('Would you like to create a droplet?. Y for us and N for no')
    if createdroplet == 'Y':
        drop.create()

    else:
        print('no new droplet. Moving on...')

def droplet_Status():
    see_status = input('Would you like to see the status of your droplets? Y for yes or N for no')
    if see_status == 'Y':
        drop_status = drop.get_action()
        for action in drop_status:
                print(action)
    elif see_status == 'N':
        print('All done!')

def main():

    get_droplets()
    new_droplet()
    droplet_Status()

main()