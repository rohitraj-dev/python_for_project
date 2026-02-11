from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://CHAI:CHAI@cluster0.lxl3fsq.mongodb.net/", tlsAllowInvalidCertificates=True)

print(client)
db = client["ytmanager"]
video_collection = db["videos"]

def add_video(name, time):
    video_collection.insert_one({"name" : name, "time": time})
    
def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")
        
def update_video(video_id, new_name, new_time):
    video_collection.delete_one({"_id": video_id})
    
def delete_video(video_id):
    video_collection.delete_one({"_id": video_id}) 
    
def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. update a videos")
        print("4. delete a video")
        print("5. Exit the App")
        choice = input("enter your choice :")
        
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("enter the video name : ")
            time = input("enter the video time : ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("enter the video id to update : ")
            name = input("enter the updated video name : ")
            time = input("enter the updated video time : ")
        elif choice == '4':
            video_id = input("enter the video id to update : ")
            delete_video(video_id, name, time)
        elif choice == '5':
            break
        else:
            print("invalid choice")
            
if __name__ == "__main__":
    main()