from datetime import datetime

__all__ = {
    'TimeUtils'
}
class TimeUtils:
    """时间类
    """
    @staticmethod
    def get_minus_day(date_now, date_past):
        days_count = (date_now - date_past).days
        return days_count
    

if __name__ == "__main__":
    date_now = datetime.now()
    date_past = datetime(2020,10,25)
    days_ = TimeUtils.get_minus_day(date_now,date_past)
    print(f"时间过去{days_}天")