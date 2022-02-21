#!/bin/bash
echo "generating proto..."
python -m grpc_tools.protoc -I=proto/ --python_out=proto/ --grpc_python_out=proto/ proto/main.proto
echo "DONE"