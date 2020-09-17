import time

def get_response_from_async(operation):
    operation_location = operation.headers["Operation-Location"]
    operation_id = operation_location.split("/")[-1]

    # Call the "GET" API and wait for it to retrieve the results 
    while True:
        get_handw_text_results = computervision_client.get_read_result(operation_id)
        if get_handw_text_results.status not in ['notStarted', 'running']:
            break
        time.sleep(1)
    
    return get_handw_text_results