//package AsyncIO;
//
//import org.apache.flink.api.common.serialization.SimpleStringSchema;
//import org.apache.flink.streaming.api.datastream.AsyncDataStream;
//import org.apache.flink.streaming.api.datastream.DataStream;
//import org.apache.flink.streaming.api.datastream.SingleOutputStreamOperator;
//import projectFlink.associatedData.ActivityBean;
//import projectFlink.associatedData.utils.FlinkUtils;
//
//import java.util.concurrent.TimeUnit;
//
//public class AsyncQueryActivityLocation {
//    public static void main(String[] args) throws Exception {
//        DataStream<String> lines = FlinkUtils.createKafkaStream(args, new SimpleStringSchema());
//
//        SingleOutputStreamOperator<ActivityBean> result = AsyncDataStream.unorderedWait(lines, new AsyncGeoToActivityBeanFunction(), 0,
//                TimeUnit.MILLISECONDS, 20);
//
//        result.print();
//
//        FlinkUtils.getEnv().execute("AsyncQueryActivityLocation");
//
//    }
//}
