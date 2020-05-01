package sink;

import org.apache.flink.streaming.api.datastream.DataStreamSource;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;

public class PrintSink {
    public static void main(String[] args) throws Exception {

        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        DataStreamSource<String> lines = env.socketTextStream("localhost", 8888);

        //subtaskIndex + 1
        lines.print("res");

        env.execute("PrintSink");
    }
}
