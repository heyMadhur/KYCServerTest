import cv2
from pyzbar import pyzbar

def capture_barcode():
    cap = cv2.VideoCapture("http://192.168.1.35:8080/video")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break
        
        # Decode the barcodes in the frame
        barcodes = pyzbar.decode(frame)
        
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type
            print(f"Found {barcode_type} barcode: {barcode_data}")
            
            # Draw the barcode
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
            cv2.putText(frame, barcode_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            
            cap.release()
            cv2.destroyAllWindows()
            return barcode_data
        
        # Display the frame
        cv2.imshow('Barcode Scanner', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    return None
