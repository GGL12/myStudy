package mapreduce.flowStatistics;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class FlowReducer extends Reducer<Text, FlowBean, Text, FlowBean> {
    private FlowBean vFlow = new FlowBean();

    @Override
    protected void reduce(Text key, Iterable<FlowBean> values, Context context) throws IOException, InterruptedException {
        long SumUpFlow = 0;
        long SumDownFlow = 0;
        //对上下行流量叠加
        for (FlowBean value : values) {
            SumUpFlow += value.getUpFlow();
            SumDownFlow += value.getDownFlow();
        }
        vFlow.set(SumUpFlow, SumDownFlow);
        context.write(key, vFlow);
    }
}
