"""
TooBit API SDK - 获取服务器时间接口示例
获取TooBit服务器时间
"""

from open_api_sdk import TooBitClient, TooBitConfig
import time
from datetime import datetime


def get_server_time():
    """获取服务器时间"""
    print("=== TooBit API 获取服务器时间接口测试 ===\n")
    
    # 创建配置 (不需要真实的API密钥来测试连接)
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    # 创建客户端
    client = TooBitClient(config)
    
    try:
        print("⏰ 获取服务器时间...")
        
        # 获取本地时间
        local_time = int(time.time() * 1000)
        local_time_str = datetime.fromtimestamp(local_time / 1000).strftime('%Y-%m-%d %H:%M:%S')
        
        print(f"   本地时间: {local_time} ({local_time_str})")
        
        # 调用获取服务器时间接口
        server_time = client.get_server_time()
        server_time_str = datetime.fromtimestamp(server_time / 1000).strftime('%Y-%m-%d %H:%M:%S')
        
        print(f"   服务器时间: {server_time} ({server_time_str})")
        
        # 计算时间差
        time_diff = abs(server_time - local_time)
        time_diff_seconds = time_diff / 1000
        
        print(f"   时间差: {time_diff} 毫秒 ({time_diff_seconds:.2f} 秒)")
        
        # 判断时间同步状态
        if time_diff < 1000:  # 1秒内
            print("✅ 时间同步状态: 优秀")
        elif time_diff < 5000:  # 5秒内
            print("✅ 时间同步状态: 良好")
        elif time_diff < 10000:  # 10秒内
            print("⚠️  时间同步状态: 一般")
        else:
            print("❌ 时间同步状态: 较差")
            print("   建议: 检查系统时间设置")
        
        print("\n🎉 获取服务器时间接口测试完成!")
        return True
        
    except Exception as e:
        print(f"❌ 获取服务器时间接口测试失败: {e}")
        return False
    
    finally:
        client.close()


if __name__ == "__main__":
    get_server_time() 