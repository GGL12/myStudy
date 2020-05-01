package sink;

import org.apache.flink.streaming.api.datastream.DataStreamSource;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.functions.sink.RichSinkFunction;
import org.apache.flink.streaming.api.functions.sink.SinkFunction;

public class addSink {
    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        DataStreamSource<String> lines = env.socketTextStream("localhost", 8888);

//        lines.addSink(new SinkFunction<String>() {
//            @Override
//            public void invoke(String value, Context context) throws Exception {
//                System.out.println("自定义Sink:" + value);
//            }
//        });
        lines.addSink(new RichSinkFunction<String>() {

            @Override
            public void invoke(String value, Context context) throws Exception {
                int subtaskIdx = getRuntimeContext().getIndexOfThisSubtask();
                System.out.println(subtaskIdx + ":" + value);
            }
        });
        env.execute("SinkSink");
    }
}
