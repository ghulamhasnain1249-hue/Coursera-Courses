import os
import re

def get_sort_key(filename):
    # اگر فائل کا نام 'subtitle' سے شروع نہیں ہوتا تو اسے آخر میں رکھنے کے لیے بڑی ترجیح (priority) دیں
    if not filename.lower().startswith("subtitle"):
        return (1, filename)
    
    # اگر نام میں نمبر موجود ہے (مثلاً subtitle (5).txt) تو وہ نمبر نکالیں
    match = re.search(r'\((\d+)\)', filename)
    if match:
        num = int(match.group(1))
    else:
        # اگر صرف 'subtitle.txt' ہے تو اسے سب سے پہلے (نمبر 0) رکھیں
        num = 0
        
    return (0, num)

def merge_txt_files(output_filename="Full-Module.txt"):
    # موجودہ فولڈر سے تمام .txt فائلیں حاصل کریں (آؤٹ پٹ فائل کو چھوڑ کر)
    files = [f for f in os.listdir('.') if f.endswith('.txt') and f != output_filename]
    
    # ترتیب دیں
    sorted_files = sorted(files, key=get_sort_key)
    
    print("فائلیں درج ذیل ترتیب میں ضم کی جا رہی ہیں:")
    for f in sorted_files:
        print(f" -> {f}")
        
    # تمام فائلوں کو ملا کر ایک بڑی فائل بنائیں
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        for fname in sorted_files:
            outfile.write(f"\n\n--- [FILE START: {fname}] ---\n\n")
            try:
                with open(fname, 'r', encoding='utf-8', errors='ignore') as infile:
                    outfile.write(infile.read())
            except Exception as e:
                print(f"خرابی: {fname} پڑھنے میں مسئلہ آیا: {e}")
                
    print(f"\nکامیابی! تمام فائلیں '{output_filename}' میں محفوظ کر دی گئی ہیں۔")

if __name__ == "__main__":
    merge_txt_files()
