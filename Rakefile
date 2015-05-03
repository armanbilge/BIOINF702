task 'assignment1' => 'assignment1.pdf'
task 'assignment3' => 'assignment3.pdf'
rule '.pdf' => '.md' do |t|
  sh "pandoc #{t.source} -o #{t.name}"
end
