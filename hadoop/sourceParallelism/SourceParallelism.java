package sourceParallelism;

import org.apache.flink.api.common.functions.FilterFunction;
import org.apache.flink.api.common.typeinfo.Types;
import org.apache.flink.streaming.api.datastream.DataStreamSource;
import org.apache.flink.streaming.api.datastream.SingleOutputStreamOperator;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.util.NumberSequenceIterator;

import java.util.Arrays;

public class SourceParallelism {
    public static void main(String[] args) throws Exception {
        /*
        实验demo下的source parallelism
         */

        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        //并行度为1的source
        //DataStreamSource<String> lines = env.socketTextStream("localhost", 8888);
        //DataStreamSource<Integer> nums = env.fromElements(1, 2, 3, 4, 5, 6, 7, 8);
        //DataStreamSource<Integer> nums = env.fromCollection(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8));

        //并行度不为1的source
        //DataStreamSource<String> lines = env.readTextFile(args[0]);
        //DataStreamSource<Long> nums = env.generateSequence(1, 100);
        DataStreamSource<Long> nums = env.fromParallelCollection(new NumberSequenceIterator(1, 100), Types.LONG);

        int parallelism = nums.getParallelism();
        System.out.println("----------------");
        System.out.println(parallelism);

        SingleOutputStreamOperator<Long> result = nums.filter(new FilterFunction<Long>() {
            @Override
            public boolean filter(Long aLong) throws Exception {
                return aLong % 2 == 0;
            }
        });

        result.print();
        env.execute("SourceParallelism");


    }
}
