import boto3
import xlrd
s3 = boto3.resource('s3',)
loc = input("Enter filename(test.xlsx)") or "test.xlsx"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)


sourcebucket =(sheet.cell_value(1, 0))
print(sourcebucket)
destinationbucket = (sheet.cell_value(1, 1))
print(destinationbucket)


def s3bucketcopy():
    bucket = s3.Bucket(sourcebucket)
    dest_bucket = s3.Bucket(destinationbucket)
    print(bucket)
    print(dest_bucket)

    for obj in bucket.objects.all():
        dest_key = obj.key
        print(dest_key)
        s3.Object(dest_bucket.name, dest_key).copy_from(CopySource = {'Bucket': obj.bucket_name, 'Key': obj.key})


s3bucketcopy()
